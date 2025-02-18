from flask import request
from App.utils.states import States
postOrderSchema = [
    'fecha_registro',
    'fecha_entrega',
    'estado'
]

class Validity:
    def validateOrderRequest(json: request):
        body = request.get_json()
        errorMessage = ''
        for key in postOrderSchema:
            if key in body:
                errorMessage+= f',{key}' if body[key] == '' else ''
            else:
                errorMessage+=f',{key}'
        if (body['estado'] == States.CANCELED.value):
            errorMessage+= ',descripcion' if 'descripcion' not in body or body['descripcion'] == '' else ''
        
        print(errorMessage)
        if (errorMessage != ''):
            errorMessage = f'The next parameters must not be empty or null {errorMessage}'
            raise Exception(errorMessage)

            


        
