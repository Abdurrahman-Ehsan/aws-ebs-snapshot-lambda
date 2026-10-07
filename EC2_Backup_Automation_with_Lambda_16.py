import boto3
import json
from datetime import datetime
import logging
# we will use to take backup of ec3 volumee in the form of snapshot

# Set up logging
Logger = logging.getLogger()
Logger.setLevel(logging.INFO)

#create a datetiestamp for the snapshot name
Snapshot_Name = "Snapshot-" + datetime.now().strftime("%Y-%m-%d-%h")
#Volume ID of the EC2 volume to take snapshot of
volume_id = 'vol-0ffafd8af6dc51e58'  # Replace with your volume ID
# Create an EC2 client
EC2_Client = boto3.client('ec2')

#create a function for lambda to take snapshot of the volume
def lambda_handler(event, context):
    try:
        #create a snapshot of the specified volume
        response = EC2_Client.create_snapshot(
            VolumeId=volume_id,
            Description='Automated snapshot created by Lambda function',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': Snapshot_Name
                        },
                    ]
                },
            ]
        )
        # Log the snapshot ID
        Logger.info(f"SnapShot Taken Successfully: {json.dumps(response, default=str)}")

    except Exception as e:
        Logger.info(f"Error creating Snapshot: {str(e)}")