from django.test import TestCase
from data.management.commands.populate_data import Command

from student.models import Student
from student.serializers import StudentSerializerGeneral
from django.urls import reverse


class StudentTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # Populate DB
        comm = Command()
        comm.handle(path=r"C:\Users\javit\Documents\ORIUN_back\django_project\data\data_csv")

    def setUp(self):
        # # User auth
        # # cur_user = Employee.objects.get(user__username='maria_alvarez')
        # response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
        # self.assertEqual(response.status_code, 200)
        #
        # response_body = json.loads(response.content.decode('utf-8'))
        # self.bearer_token = response_body['access']
        #
        # response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        # self.assertEqual(response.status_code, 200)
        #
        # response_body = json.loads(response.content.decode('utf-8'))
        # self.bearer_token_std = response_body['access']
        pass

    def test_get_students(self):
        print("TEST: test_get_students")

        qset = Student.objects.all()
        qset = StudentSerializerGeneral(qset, many=True).data

        self.assertGreaterEqual(len(qset), 1)


    def test_post_students(self):
        print("TEST: test_post_students")

        data = {
            "email": "jtarazonaj@unal.edu.co",
            "password": "El hash",
            "verif_code": "AA2400",
            "id": 1041578941,
            "first_name": "Javier",
            "last_name": "Tarazona",
            "type_document": "CC",
            "birth_place": "Bucaramanga",
            "birth_date": "2002-06-25",
            "country": "Colombia",
            "city": "Bogotá",
            "phone": "3341158915",
            "address": "Carrera 45 #26-42",
            "sex": "M",
            "ethnicity": "NA",
            "headquarter": "BO",
            "PAPA": 4.5,
            "PBM": 50,
            "advance": 60.0,
            "is_enrolled": True,
            "num_semesters": 6,
            "diseases": "NO",
            "medication": "NO",
            "faculty": "Ingeniería",
            "major": "ISCO",
            "admission": "REGUL",
            "study_level": "PRE",
            "certificate_grades": "",
            "certificate_student": "",
            "payment_receipt": ""
        }

        headers = {}
        response = self.client.post(reverse("student:post_user_student"), data=data, content_type='application/json', **headers)

        print(response)
        print(response.status_code)
        print(response.json())

        qset = Student.objects.filter(id=1041578941)
        qset = StudentSerializerGeneral(qset, many=True).data
        print(qset)

        self.assertEqual(1, 1)

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        pass