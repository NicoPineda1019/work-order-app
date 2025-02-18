from flask import Flask
from App.router import routes
import awsgi

app = Flask(__name__)
app.register_blueprint(routes.bp)

def handler(event, context):
    print(event)
    return awsgi.response(app, event, context)