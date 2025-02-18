import boto3

client = boto3.client('sns', region_name='us-east-1')

class Sns:
    def send(Topic, Subject, Message, MessageAttributes, MsgId):
        try:
            client.publish(
                TopicArn=Topic,
                Subject=Subject,
                Message=Message,
                MessageAttributes=MessageAttributes
            )
        except Exception as e:
            print(f'{e}')