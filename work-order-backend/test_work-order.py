import os
import pytest
import config
from app import app as App
import boto3 
from App.services import dynamoDb
from App.services import snsMessage
import unittest
from unittest.mock import Mock


class workorder_test(unittest.TestCase):

    def test_create_order_success(self):
        with App.test_client() as client:
            mockdyn = Mock()
            dynamoDb.dynamodb_client = Mock()
            snsMessage.client = Mock()
            mockdyn.put_item.return_value={''}
            response = client.post("/v1/order", json={
                "fecha_registro": "2025-02-15",
                "fecha_entrega": "2025-02-20",
                "descripcion": "Comp",
                "estado": "CANCELADA"
            })
            assert response.status_code == 200

    def test_create_order_badrequest(self):
        with App.test_client() as client:
            response = client.post("/v1/order", json={
                "fecha_entrega": "2025-02-20",
                "descripcion": "Comp",
                "estado": "CANCELADA"
            })
            assert response.status_code == 400