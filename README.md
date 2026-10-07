# AWS EBS Snapshot Automation

A Python automation script that uses the AWS SDK for Python (Boto3) to create Amazon EBS snapshots for backup purposes.

## Overview

This project automates the creation of an EBS snapshot from a specified Amazon EBS volume.

The script:

1. Identifies the target EBS volume.
2. Verifies that the volume exists.
3. Creates an EBS snapshot.
4. Retrieves the generated Snapshot ID.
5. Displays the snapshot creation result.

This project was built as a hands-on exercise in AWS automation with Python and Boto3.

## Architecture

```text
Python Script
     |
     v
   Boto3
     |
     v
Amazon EC2 API
     |
     v
Amazon EBS Volume
     |
     v
EBS Snapshot