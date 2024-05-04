from django.test import TestCase
from data.management.commands.populate_data import Command

from student.models import Student
from django.urls import reverse
import requests


def sep_test_request_verif_code(id, email):
    print("TEST: test_request_verif_code")

    data = {
        "id": id,
        "email": email
    }

    headers = {}
    url = "http://localhost:8000/person/code/"
    response = requests.post(url, json=data, headers=headers)

    print(response)
    print(response.status_code)
    print(response.json())

    if not (response.status_code == 200):
         raise ValueError("In sep_test_request_verif_code: response.status_code != 200")
    if not (response.json() == {'mensaje': 'Se envió el código de verificación al correo indicado'}):
        raise ValueError("In sep_test_request_verif_code: response.json() != {'mensaje': 'Se envió el código de verificación al correo indicado'")


# class PersonTestCase(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         # Populate DB
#         comm = Command()
#         comm.handle(path=r"data\data_csv")
#         pass
#
#     def setUp(self):
#         # # User auth
#         # # cur_user = Employee.objects.get(user__username='maria_alvarez')
#         # response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
#         # self.assertEqual(response.status_code, 200)
#         #
#         # response_body = json.loads(response.content.decode('utf-8'))
#         # self.bearer_token = response_body['access']
#         #
#         # response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
#         # self.assertEqual(response.status_code, 200)
#         #
#         # response_body = json.loads(response.content.decode('utf-8'))
#         # self.bearer_token_std = response_body['access']
#         pass
#
#     def sep_test_request_verif_code(self):
#         print("TEST: test_request_verif_code")
#
#         data = {
#             "id": 1021632167,
#             "email": "jtarazonaj@unal.edu.co"
#         }
#
#         headers = {}
#         response = self.client.post(reverse("person:request_verif_code"), data=data, headers=headers)
#
#         print(response)
#         print(response.status_code)
#         print(response.json())
#
#         self.assertGreaterEqual(response.status_code, 200)
#         self.assertGreaterEqual(response.json(), {'mensaje': 'Se envió el código de verificación al correo indicado'})
#
#     def tearDown(self):
#         pass
#
#
#     @classmethod
#     def tearDownClass(cls):
#         pass