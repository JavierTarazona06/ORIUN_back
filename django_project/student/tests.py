from django.test import TestCase
from data.management.commands.populate_data import Command

from student.models import Student
from student.serializers import StudentSerializerGeneral
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class StudentTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # Populate DB
        # comm = Command()
        # comm.handle(path=r"data\data_csv")
        pass

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

        with open("data/forms/templates/Certificado_Notas.pdf", 'rb') as grades_file:
            grades_data = grades_file.read()
            grades_obj = SimpleUploadedFile("Certificado_Notas.pdf", grades_data)

        with open("data/forms/templates/Matricula_Unal.pdf", 'rb') as student_file:
            student_data = student_file.read()
            student_obj = SimpleUploadedFile("Certificado_Matricula_Estudiante.pdf", student_data)

        with open("data/forms/templates/ReciboPago.pdf", 'rb') as payment_file:
            payment_data = payment_file.read()
            payment_obj = SimpleUploadedFile("Recibo_Pago.pdf", payment_data)

        data = {
            "email": "jtarazonaj@unal.edu.co",
            "password": "El hash",
            "verif_code": "AA2400",
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
                {'id': 16,
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
            'study_level': 'PRE', 'contact_person': None, 'calls_done': []
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensaje': 'Estudiante creado exitosamente'})
        self.assertEqual(qset, qsetr)

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        pass