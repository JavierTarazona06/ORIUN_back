import os
import json

from django.test import TestCase
from django.test import TestCase
from django.urls import reverse

from data.management.commands.populate_data import Command

from .models import Traceability
from .serializers import TraceabilitySerializer

from call.models import Call

class TraceTestCase(TestCase):

    @classmethod
    def setUpClass(cls):

        if Call.objects.count() == 0:
            command = Command()
            command.handle(path=os.path.join('data', 'data_csv'))

    def setUp(self):
        # User auth
        # cur_user = Employee.objects.get(user__username='maria_alvarez')
        response = self.client.post('/api-token/', {'username': 'maria.alvarez@unal.edu.co', 'password': 'Maria#1234'})
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token = response_body['access']

        response = self.client.post('/api-token/',
                                    {'username': 'santiago.garcia@unal.edu.co', 'password': 'Password123'})
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token_std = response_body['access']

        response = self.client.post('/api-token/', {'username': 'vmoras@unal.edu.co', 'password': '123456'})
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token_std_vale = response_body['access']

    def test_get_traceability(self):
        print("test_get_traceability")

        qset = Traceability.objects.all()
        qset = TraceabilitySerializer(qset, many=True).data

        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        response = self.client.get(reverse("traceability:get_trace"), headers=headers)

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),qset)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass