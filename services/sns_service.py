import boto3
from config import AWS_REGION, SNS_TOPIC_ARN

sns = boto3.client("sns", region_name=AWS_REGION)

def send_notification(message):
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="MedTrack Notification"
    )
