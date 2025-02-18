import os
import boto3

ORDERS_TABLE = os.environ['USERS_TABLE']
dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')

class DynamoService:

    @staticmethod
    def putItem(data):
        response = False
        try:
            dynamodb_client.put_item(
                TableName=ORDERS_TABLE,
                Item=data
            )
            response = True
        except Exception as e:
            print(f'{e}')

        return response


