# 🤖 My ChatBot – SlackBot for AWS Automation

Welcome to **CloudOpsBot**, a powerful Slack-integrated chatbot that enables you to manage AWS resources directly from your Slack workspace. It’s designed for DevOps automation, real-time cloud control, and easy extensibility.

---

## 🚀 Project Overview

**CloudOpsBot** is a smart Python-based Slack bot that allows you to control and monitor AWS services like EC2, S3, and CloudWatch using natural Slack commands.

Whether you're deploying EC2 instances, fetching logs, or managing auto-scaling, this bot simplifies cloud operations through intuitive chat-based interactions.

---

## 💡 Key Features

- **EC2 Instance Management**
  - Launch, list, stop, start, reboot, and terminate EC2 instances
  - Get public IP and status updates
- **Auto-Scaling**
  - Automatically create EC2 instances when CPU > 80%
- **CloudWatch Logs**
  - Fetch application/system logs and post to Slack
- **S3 Bucket Operations**
  - Create and list S3 buckets
- **Server Health Monitoring**
  - Perform periodic health checks
- **Security Tools**
  - IAM policy audits
  - Basic port scanning
- **Extensible Architecture**
  - Azure and Kubernetes integration placeholders included

---

## 💬 Available Slack Commands

| Command | Description |
|--------|-------------|
| `/cloudopsbot launch` | Launch a new EC2 instance |
| `/cloudopsbot list` | List all EC2 instances |
| `/cloudopsbot stop` | Stop the SlackBot EC2 instance |
| `/cloudopsbot start` | Start the SlackBot EC2 instance |
| `/cloudopsbot reboot` | Reboot the EC2 instance |
| `/cloudopsbot status` | Check EC2 instance status and public IP |
| `/cloudopsbot terminate` | Terminate the EC2 instance |
| `/cloudopsbot s3 create <bucket-name>` | Create an S3 bucket |
| `/cloudopsbot s3 list` | List all S3 buckets |

> 🔧 More commands and features coming soon!

---

## 🛠️ Tech Stack

- **Language**: Python
- **Framework**: Flask
- **Cloud SDK**: AWS Boto3
- **Messaging Platform**: Slack (Bolt SDK)
- **Infrastructure Tools**: AWS CLI, IAM, CloudWatch
- **Optional**: Terraform for IaC

---

![Screenshot](Screenshot (9).png)



