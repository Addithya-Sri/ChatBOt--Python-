Welcome to CloudOpsBot, a powerful Slack-integrated chatbot that lets you automate AWS operations straight from your Slack workspace.

🚀 Project Overview
SlackBot for AWS Automation is a chatbot built with Python and Flask, integrated with Slack via the Slack-Bolt SDK. It empowers developers and DevOps engineers to manage cloud infrastructure — like EC2 and S3 — using natural Slack commands.

💡 Key Features
⚙️ EC2 Instance Control: Launch, list, stop, start, reboot, terminate, and check the status of EC2 instances via Slack.

🧠 Auto-Scaling: Spin up new EC2 instances automatically when CPU usage exceeds a threshold.

🗃️ S3 Bucket Operations: Create and list S3 buckets from within Slack.

📄 CloudWatch Logs: Fetch logs and send them to Slack channels.

📈 Health Monitoring: Run health checks on your servers.

🔐 Security Checks: IAM permission audits and basic port scan capabilities.

☁️ Multi-Cloud Ready: Azure and Kubernetes integrations scaffolded for future expansion.

💬 Available Slack Commands
Here are all the commands you can use with your current /cloudopsbot setup:

🖥️ EC2 Commands
/cloudopsbot launch — Launch a new EC2 instance.

/cloudopsbot list — List all EC2 instances.

/cloudopsbot stop — Stop the SlackBot EC2 instance.

/cloudopsbot start — Start the SlackBot EC2 instance.

/cloudopsbot reboot — Reboot the SlackBot EC2 instance.

/cloudopsbot status — Get status and public IP of the EC2 instance.

/cloudopsbot terminate — Terminate the SlackBot EC2 instance.

📦 S3 Bucket Commands
/cloudopsbot s3 create <bucket-name> — Create a new S3 bucket.

/cloudopsbot s3 list — List all your S3 buckets.

🛠️ Tech Stack
Python with Flask

Slack-Bolt SDK

AWS Boto3

🧑‍💻 Getting Started
Clone the repo

Set up your AWS credentials and IAM roles

Create a Slack app and connect it to your workspace

Run the Flask app and start automating!

