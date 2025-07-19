import boto3

ec2 = boto3.resource('ec2')
s3 = boto3.client("s3")

def launch_ec2_instance():
    instance = ec2.create_instances(
        ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[
            {'ResourceType': 'instance', 'Tags': [{'Key': 'Name', 'Value': 'SlackBot-Instance'}]}
        ]
    )
    instance_id = instance[0].id
    return f"Launched EC2 Instance with ID: {instance_id}"

def stop_ec2_instance(instance_id):
    instance = ec2.Instance(instance_id)
    response = instance.stop()
    return f"Stopping instance {instance_id}."

def start_ec2_instance(instance_id):
    instance = ec2.Instance(instance_id)
    response = instance.start()
    return f"Starting instance {instance_id}."

def reboot_ec2_instance(instance_id):
    instance = ec2.Instance(instance_id)
    response = instance.reboot()
    return f"Rebooting instance {instance_id}."

def get_slackbot_instances():
    filters = [
        {'Name': 'tag:Name', 'Values': ['SlackBot-Instance']},
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ]
    instances = ec2.instances.filter(Filters=filters)
    return [instance.id for instance in instances]


def list_all_instances():
    instances = ec2.instances.all()
    details = []

    for instance in instances:
        name_tag = next((tag["Value"] for tag in instance.tags or [] if tag["Key"] == "Name"), "N/A")
        details.append(
            f"• ID: `{instance.id}` | Name: *{name_tag}* | State: `{instance.state['Name']}` | Type: `{instance.instance_type}`"
        )

    return "\n".join(details) if details else "🚫 No EC2 instances found."

def terminate_ec2_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.terminate()
    return f"⚠️ Terminating instance `{instance_id}`. This action cannot be undone."

def create_s3_bucket(bucket_name):
    session = boto3.session.Session()
    current_region = session.region_name or 'us-east-1'

    s3_client = session.client('s3', region_name=current_region)

    try:
        if current_region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': current_region}
            )
        return f"✅ Created S3 bucket: `{bucket_name}` in region `{current_region}`"
    except Exception as e:
        return f"❌ Failed to create bucket `{bucket_name}`: {str(e)}"
    
def list_s3_buckets():
    try:
        response = s3.list_buckets()
        buckets = response.get("Buckets", [])
        if not buckets:
            return "🚫 No S3 buckets found."
        
        bucket_names = [bucket["Name"] for bucket in buckets]
        return "📦 S3 Buckets:\n" + "\n".join(f"• {name}" for name in bucket_names)
    except Exception as e:
        return f"❌ Failed to list buckets: {str(e)}"
    
    

    
    

      
            
        
    



