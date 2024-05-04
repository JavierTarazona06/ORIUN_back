import os
import student
from call.models import Call
from django.test import TestCase
from data.constants import Constants
from student.models import ContactPerson
from data.management.commands.populate_data import Command


class StudentTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        if Call.objects.count() == 0:
            command = Command()
            command.handle(path=os.path.join('data', 'data_csv'))

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

    @classmethod
    def tearDownClass(cls):
        pass
