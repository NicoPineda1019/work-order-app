import os
import json
from flask import request
import uuid
from App.utils.mapp import Mapp
from App.services.dynamoDb import DynamoService as dynServ
from App.services.snsMessage import Sns

SNS_TOPIC = os.environ['SNS_TOPIC']
SNS_SUBJECT = 'WORK_ORDERS'
class Order:
    def process(request:request):
        data = request.get_json()
        id = uuid.uuid1()
        idObject = {'id': str(id)}
        dynamoJson = Mapp.toDynamo({**data, **idObject})
        response = dynServ.putItem(dynamoJson)
        if (not response):
            return {'error': 'Could not create order by error in server'}, 500
        
        state = data['estado']
        Sns.send(SNS_TOPIC, SNS_SUBJECT, json.dumps(idObject), {'estado' : {'DataType': 'String.Array', 'StringValue': f'["{state}"]'}}, idObject['id'])
        return {'message': f'Order registered with id:{id}' }, 200