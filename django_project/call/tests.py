import json

from django.test import TestCase
from django.urls import reverse
from call.models import Call
from employee.models import Employee
from data.management.commands.populate_data import Command
from call.serializers import CallSerializer

import requests

class CallsTestCase2(TestCase):

    @classmethod
    def setUpClass(cls):
        # Populate DB
        comm = Command()
        comm.handle(path=r"C:\Users\javit\Documents\ORIUN_back\django_project\data\data_csv")

    def setUp(self):
        # User auth
        # cur_user = Employee.objects.get(user__username='maria_alvarez')
        response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
        self.assertEqual(response.status_code, 200)

        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token = response_body['access']

        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        self.assertEqual(response.status_code, 200)

        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token_std = response_body['access']

    # 1: Get Call: Employee
    def test_get_all_calls_noauth(self):
        """
        Return all calls without auth
        """
        print("TEST: test_get_all_calls_noauth")

        response = self.client.get(reverse("call:calls_list"))

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'Authentication credentials were not provided.'})

    def test_get_all_calls_wrong_auth(self):
        """
        Return all calls with wrong auth
        """
        print("TEST: test_get_all_calls_wrong_auth")

        authorization_header = {"HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"}
        response = self.client.get(reverse("call:calls_list"), **authorization_header)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_get_all_calls(self):
        """
        Return all calls with
        """
        print("TEST: test_get_all_calls_auth")

        authorization_header = {"HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"}
        response = self.client.get(reverse("call:calls_list"), **authorization_header)

        queryset = Call.objects.all()
        serializer = CallSerializer(queryset, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)

    # 2: Post Call: Employee

    def test_post_call_noauth(self):
        print("TEST: test_post_call_noauth")

        data = {
            "format": "V",
            "study_level": "PRE",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {}

        response = self.client.post(reverse("call:calls_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'Authentication credentials were not provided.'})

    def test_post_call_wrongauth(self):
        print("TEST: test_post_call_wrongauth")

        data = {
            "format": "V",
            "study_level": "PRE",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.bearer_token_std}"
        }

        response = self.client.post(reverse("call:calls_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_post_call(self):
        print("TEST: test_post_call")

        data = {
            "format": "V",
            "study_level": "PRE",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.bearer_token}"
        }

        response = self.client.post(reverse("call:calls_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['mensaje'], 'Convocatoria creada exitosamente')

    # 3. Get Call by ID: Employee

    def test_get_call_wrgauth(self):
        """
        Return call with given id wrong auth
        """
        print("TEST: test_get_call_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:calls_detail", args=[2]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_get_call(self):
        """
        Return call with given id
        """
        print("TEST: test_get_call")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_detail", args=[2]), **headers)

        queryset = Call.objects.get(pk=2)
        serializer = CallSerializer(queryset, many=False)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)


    # 4. Update Call: Employee

    def test_put_call(self):
        print("TEST: test_put_call")

        queryset = Call.objects.get(pk=2)
        serializer = CallSerializer(queryset, many=False)
        study_level1 = serializer.data['study_level']

        data = {
            "format": "V",
            "study_level": "POS",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.put(reverse("call:calls_update_by_id", args=[2]), data=data, content_type='application/json', **headers)


        queryset = Call.objects.get(pk=2)
        serializer = CallSerializer(queryset, many=False)
        study_level2 = serializer.data['study_level']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"mensaje": "Convocatoria actualizada exitosamente"})
        self.assertNotEqual(study_level1, study_level2)
        self.assertEqual("Postgrado", study_level2)

    def test_put_no_call(self):
        print("TEST: test_put_no_call")

        data = {
            "format": "V",
            "study_level": "POS",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.put(reverse("call:calls_update_by_id", args=[15]), data=data, content_type='application/json', **headers)


        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'La convocatoria especificada no existe'})

    def test_put_call_no_uni(self):
        print("TEST: test_put_call_no_uni")

        data = {
            "format": "V",
            "study_level": "POS",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 15
        }

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.put(reverse("call:calls_update_by_id", args=[2]), data=data,
                                   content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'La universidad especificada no existe'})

    # 5. Delete Call: Employee

    def test_delete_nocall(self):
        print("TEST: test_delete_nocall")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.delete(reverse("call:calls_detail", args=[0]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"error": "No Call matches the given query."})


    def test_delete_call(self):
        print("TEST: test_delete_call")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.delete(reverse("call:calls_detail", args=[8]), **headers)

        print(response.status_code)
        print(response.json())

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json(), {'mensaje': 'Convocatoria eliminada satisfactoriamente'})


    @classmethod
    def tearDownClass(cls):
        pass