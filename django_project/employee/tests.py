import json

from django.test import TestCase
from data.management.commands.populate_data import Command

from .models import Employee
from .serializers import EmployeeSerializerGeneral
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from person.tests import sep_test_request_verif_code
from django.db import connections
from django.test.utils import teardown_databases
from django.db import connection
from student.models import Student

class EmployeeTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(EmployeeTestCase, cls).setUpClass()

        qset_students = Student.objects.all()
        if not qset_students:
            # Populate DB
            comm = Command()
            comm.handle(path=r"data\data_csv")

    def setUp(self):
        # User auth
        # cur_user = Employee.objects.get(user__username='maria_alvarez')
        response = self.client.post('/api-token/', {'username': 'maria.alvarez@unal.edu.co', 'password': 'Maria#1234'})
        self.assertEqual(response.status_code, 200)

        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token = response_body['access']

        response = self.client.post('/api-token/', {'username': 'santiago.garcia@unal.edu.co', 'password': 'Password123'})
        self.assertEqual(response.status_code, 200)

        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token_std = response_body['access']
        pass

    def test_get_employees(self):
        print("TEST: test_get_employees")

        qset = Employee.objects.all()
        qset = EmployeeSerializerGeneral(qset, many=True).data

        self.assertGreaterEqual(len(qset), 1)

    def test_post_employees(self):
        print("TEST: test_post_employees")

        sep_test_request_verif_code(1003825162, "ksierram@unal.edu.co")
        code_file_name = r"data/{}_verif_code.txt".format(1003825162)
        with open(code_file_name, "r") as file:
            code_stored = file.read()

        data = {
            "email": "ksierram@unal.edu.co",
            "password": "El hash",
            "verif_code": code_stored,
            "id": 1003825162,
            "first_name": "Karem",
            "last_name": "Sierra",
            "type_document": "CC",
            "birth_place": "Zipaquira",
            "birth_date": "2003-06-25",
            "country": "Colombia",
            "city": "Bogotá",
            "phone": "3341158916",
            "address": "Carrera 48 #26-42",
            "sex": "F",
            "ethnicity": "NA",
            "headquarter": "BO",
            "dependency": "ORI"
        }

        headers = {}
        response = self.client.post(reverse("employee:post_user_employee"), data=data, headers=headers)

        qset = Employee.objects.filter(id=1003825162)
        qset = EmployeeSerializerGeneral(qset, many=True).data[0]
        qset = qset.copy()
        del qset["user"]["password"]
        qsetr = {
            'id': 1003825162,
            'user':
                {'id': 18,
                 'username': 'ksierram@unal.edu.co',
                 'email': 'ksierram@unal.edu.co',
                 'first_name': 'Karem',
                 'last_name': 'Sierra',
                 'is_active': True,
                 'is_staff': False},
            'birth_place': 'Zipaquira',
            'country': 'Colombia','city': 'Bogotá', 'phone': '3341158916',
            'address': 'Carrera 48 #26-42', 'birth_date':'2003-06-25',
            'type_document': 'CC', 'sex': 'F', 'ethnicity': 'NA', 'headquarter': 'BO',
            "dependency": "ORI"
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensaje': 'Funcionario creado exitosamente'})
        self.assertEqual(qset, qsetr)

    def test_get_employee_by_id(self):
        print("TEST: test_get_employee_by_id")

        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        response = self.client.get(reverse("employee:read_user_employee", args=[1003235916]), headers=headers)

        qset = response.json()

        qsetr = {
            'email': 'camunozv@unal.edu.co', 'first_name': 'Carlos', 'last_name': 'Muñoz', 'id': 1003235916,
            'birth_place': 'Cali', 'country': 'Colombia', 'city': 'Bogota', 'phone': '315 425 9578',
            'address': 'Carrera 35 # 25-35', 'birth_date': '2002-04-15', 'type_document': 'CC', 'sex': 'M',
            'ethnicity': 'NA', 'headquarter': 'BO', 'dependency': 'ORI'
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        pass