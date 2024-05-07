import json

from django.test import TestCase
from data.management.commands.populate_data import Command

from student.models import Student
from student.serializers import StudentSerializerGeneral
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from person.tests import sep_test_request_verif_code


class StudentTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
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

        response = self.client.post('/api-token/', {'username': 'vmoras@unal.edu.co', 'password': '123456'})
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token_std_vale = response_body['access']

    def test_get_students(self):
        print("TEST: test_get_students")

        qset = Student.objects.all()
        qset = StudentSerializerGeneral(qset, many=True).data

        self.assertGreaterEqual(len(qset), 1)

    def test_post_students(self):
        print("TEST: test_post_students")

        with open("data/test_files/Certificado_Notas.pdf", 'rb') as grades_file:
            grades_data = grades_file.read()
            grades_obj = SimpleUploadedFile("Certificado_Notas.pdf", grades_data)

        with open("data/test_files/Matricula_Unal.pdf", 'rb') as student_file:
            student_data = student_file.read()
            student_obj = SimpleUploadedFile("Certificado_Matricula_Estudiante.pdf", student_data)

        with open("data/test_files/ReciboPago.pdf", 'rb') as payment_file:
            payment_data = payment_file.read()
            payment_obj = SimpleUploadedFile("Recibo_Pago.pdf", payment_data)

        sep_test_request_verif_code(1021632167, "jtarazonaj@unal.edu.co")
        code_file_name = r"data/{}_verif_code.txt".format(1021632167)
        with open(code_file_name, "r") as file:
            code_stored = file.read()

        data = {
            "email": "jtarazonaj@unal.edu.co",
            "password": "El hash",
            "verif_code": code_stored,
            "id": 1021632167,
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
            "PAPA": 4.8,
            "PBM": 88,
            "advance": 58.8,
            "is_enrolled": True,
            "num_semesters": 7,
            "diseases": "NO",
            "medication": "NO",
            "faculty": "Ingeniería",
            "major": "ISCO",
            "admission": "REGUL",
            "study_level": "PRE",
            "certificate_grades": grades_obj,
            "certificate_student": student_obj,
            "payment_receipt": payment_obj
        }

        headers = {}
        response = self.client.post(reverse("student:post_user_student"), data=data, headers=headers)

        qset = Student.objects.filter(id=1021632167)
        qset = StudentSerializerGeneral(qset, many=True).data[0]
        qset = qset.copy()
        del qset["user"]["password"]
        qsetr = {
            'id': 1021632167,
            'user':
                {'id': 19,
                 'username': 'jtarazonaj@unal.edu.co',
                 'email': 'jtarazonaj@unal.edu.co',
                 'first_name': 'Javier',
                 'last_name': 'Tarazona',
                 'is_active': True,
                 'is_staff': False},
            'birth_place': 'Bucaramanga',
            'country': 'Colombia','city': 'Bogotá', 'phone': '3341158915',
            'address': 'Carrera 45 #26-42', 'birth_date':'2002-06-25',
            'type_document': 'CC', 'sex': 'M', 'ethnicity': 'NA', 'headquarter': 'BO', 'PAPA': 4.8,
            'PBM': 88, 'advance': 58.8, 'is_enrolled': True, 'date_banned_mobility': '2000-01-01', 'num_semesters': 7,
            'diseases': 'NO', 'medication': 'NO', 'faculty': 'Ingeniería', 'major': 'ISCO', 'admission': 'REGUL',
            'study_level': 'PRE', 'contact_person': None
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensaje': 'Estudiante creado exitosamente'})
        self.assertEqual(qset, qsetr)

    def test_get_student_by_id(self):
        print("TEST: test_get_student_by_id")

        headers = {"Authorization": f"Bearer {self.bearer_token_std_vale}"}
        response = self.client.get(reverse("student:read_user_student", args=[1013691479]), headers=headers)

        qset = response.json()
        if "certificate_grades" in qset:
            qset["certificate_grades"] = ''
        if "certificate_student" in qset:
            qset["certificate_student"] = ''
        if "payment_receipt" in qset:
            qset["payment_receipt"] = ''

        qsetr = {
            'email': 'vmoras@unal.edu.co', 'first_name': 'Valeria', 'last_name': 'Mora', 'id': 1013691479,
            'birth_place': 'Bogota', 'country': 'Colombia', 'city': 'Bogota', 'phone': '315 354 6587',
            'address': 'Carrera 45 # 27-12', 'birth_date': '1999-06-15', 'type_document': 'CC', 'sex': 'F', 'ethnicity': 'NA', 'headquarter': 'BO',
            'PAPA': 4.6, 'PBM': 42, 'advance': 55.8, 'is_enrolled': True, 'date_banned_mobility': '2000-01-01',
            'num_semesters': 5, 'diseases': None, 'medication': None, 'faculty': 'Ingeniería', 'major': 'ISCO', 'admission': 'REGUL',
            'study_level': 'PRE', 'calls_done': [], 'certificate_grades': '', 'certificate_student': '', 'payment_receipt': ''
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass