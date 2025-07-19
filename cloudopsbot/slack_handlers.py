from slack_bolt import App
import boto3
import re
from cloud.aws import (
    launch_ec2_instance,
    stop_ec2_instance,
    start_ec2_instance,
    reboot_ec2_instance,
    get_slackbot_instances,
    list_all_instances,
    terminate_ec2_instance,
    create_s3_bucket,
    list_s3_buckets
)

ec2 = boto3.resource("ec2")

def register_handlers(app: App):

    @app.command("/cloudopsbot")
    def handle_cloudops_command(ack, respond, command):
        ack()
        text = command.get("text", "").strip().lower()

        if text == "launch":
            respond(launch_ec2_instance())
            return

        if text == "list":
            respond(list_all_instances())
            return

        # Handle S3 subcommands
        if text.startswith("s3"):
            parts = text.split()
            if len(parts) < 2:
                respond("⚠️ Please specify an s3 subcommand like: create, list, upload, etc.")
                return

            subcommand = parts[1]

            if subcommand == "create":
                if len(parts) < 3:
                    respond("⚠️ Please provide a bucket name like: `/cloudopsbot s3 create my-bucket-name`")
                    return
                bucket_name = parts[2]
                respond(create_s3_bucket(bucket_name))
                return

            elif subcommand == "list":
                respond(list_s3_buckets())
                return

            respond(f"⚠️ Unknown s3 subcommand `{subcommand}`. Try: create, list")
            return

        # Handle EC2 actions
        instances = get_slackbot_instances()
        if not instances:
            respond("❌ No SlackBot EC2 instances found.")
            return

        instance_id = instances[0]

        if text == "stop":
            respond(stop_ec2_instance(instance_id))
        elif text == "start":
            respond(start_ec2_instance(instance_id))
        elif text == "reboot":
            respond(reboot_ec2_instance(instance_id))
        elif text == "status":
            instance = ec2.Instance(instance_id)
            state = instance.state["Name"]
            ip = instance.public_ip_address or "No public IP assigned"
            respond(f"📦 Instance `{instance_id}` is currently *{state}*.\n🌐 Public IP: `{ip}`")
        elif text == "terminate":
            respond(terminate_ec2_instance(instance_id))
        else:
            respond("⚠️ Unknown command. Try: launch, stop, start, reboot, status, list, terminate")
