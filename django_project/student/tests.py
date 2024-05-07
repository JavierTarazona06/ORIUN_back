import os
import student
from call.models import Call
from django.test import TestCase
from data.constants import Constants
from student.models import ContactPerson
from data.management.commands.populate_data import Command
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
    # TODO: add data_banned_mobility and max_applications

    def test_eligibility_authentication(self):
        """
        Makes sure only students can access their eligibility data.
        """
        response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
        response = self.client.get(
            '/student/eligible/', headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['detail'], 'Current user is not a student')

    def test_eligibility_registration(self):
        """
        Makes sure the student is enrolled.
        """
        response = self.client.post('/api-token/', {'username': 'nicolas_ramirez', 'password': 'shakira101'})
        response = self.client.get(
            '/student/eligible/', headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['eligibility'])
        self.assertEqual(response.json()['message'], 'Necesita estar matriculado o en reserva de cupo')

    def test_eligibility_papa(self):
        """
        Makes sure the student has enough PAPA.
        """
        response = self.client.post('/api-token/', {'username': 'isabella_gonzalez', 'password': 'Pasword021'})
        response = self.client.get(
            '/student/eligible/', {'call': 1}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['eligibility'])
        self.assertEqual(response.json()['message'], 'PAPA insuficiente')

    def test_eligibility_level(self):
        """
        Makes sure that the student has the correct study level for the call
        """
        response = self.client.post('/api-token/', {'username': 'camila_perez', 'password': 'qwertY'})
        response = self.client.get(
            '/student/eligible/', {'call': 1}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['eligibility'])
        self.assertEqual(response.json()['message'], 'Usted no pertenece al nivel de estudios necesario')

    def test_eligibility_num_semesters(self):
        """
        Makes sure that for Uniandes calls the student has the correct number of semesters
        """
        response = self.client.post('/api-token/', {'username': 'juanpablo_lopez', 'password': 'abc123'})
        response = self.client.get(
            '/student/eligible/', {'call': 1}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['eligibility'])
        self.assertEqual(response.json()['message'], 'Para esta convocatoria necesita minimo 2 semestres cursados')

    def test_eligibility_advance(self):
        """
        Makes sure the student has enough advance
        """
        response = self.client.post('/api-token/', {'username': 'andres_hernandez', 'password': 'pass1234'})
        response = self.client.get(
            '/student/eligible/', {'call': 2}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['eligibility'])
        self.assertEqual(response.json()['message'], 'Avance insuficiente')

    def test_eligibility_correct(self):
        """
        If the student has all the requirements, they can apply
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        response = self.client.get(
            '/student/eligible/', {'call': 1}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['eligibility'])
        self.assertEqual(response.json()['message'], '')

    def test_info_student(self):
        """
        Checks basic student info, such as contact_person, health info and info_coordinator
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        response = self.client.get(
            '/student/info_application/', headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        contact_person = student.serializers.ContactPersonSerializer(ContactPerson.objects.get(id=1))
        self.assertEqual(response.json()['contact_person'], contact_person.data)
        self.assertEqual(response.json()['diseases'], 'diabetes')
        self.assertEqual(response.json()['medication'], None)
        info_coordinator = Constants.INFO_FACULTIES['Bogotá']['Facultad de Ciencias Agrarias']['Medicina Veterinaria']
        self.assertEqual(response.json()['info_coordinator'], info_coordinator)

        # TODO: Make someone without contact_person information

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

        headers = {"Authorization": f"Bearer {self.bearer_token_std}"}
        response = self.client.get(reverse("student:read_user_student", args=[1013691479]), headers=headers)
        print(response.json())

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
