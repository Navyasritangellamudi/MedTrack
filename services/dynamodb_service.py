import boto3
from config import AWS_REGION, DYNAMODB_TABLE

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

def register_user(user):
    table.put_item(Item=user)

def get_user(email):
    response = table.get_item(Key={"email": email})
    return response.get("Item")
