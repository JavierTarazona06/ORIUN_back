import os
from call.models import Call
from django.test import TestCase
from data.management.commands.populate_data import Command


class SigninTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        if Call.objects.count() == 0:
            command = Command()
            command.handle(path=os.path.join('data', 'data_csv'))

    def test_login_student(self):
        """
        Checks that login returns 2 tokens (refresh and access) and type_user is student
        """
        print("TEST:test_login_student")
        response = self.client.post(
            '/api-token/', {'username': 'santiago.garcia@unal.edu.co', 'password': 'Password123'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'refresh')
        self.assertContains(response, 'access')
        self.assertContains(response, 'type_user')
        self.assertEqual(response.json()['type_user'], 'student')

    def test_login_employee(self):
        """
        Checks that login returns 2 tokens (refresh and access) and type_user is employee
        """
        print("TEST:test_login_employee")
        response = self.client.post(
            '/api-token/', {'username': 'maria.alvarez@unal.edu.co', 'password': 'Maria#1234'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'refresh')
        self.assertContains(response, 'access')
        self.assertContains(response, 'type_user')
        self.assertEqual(response.json()['type_user'], 'employee')

    def test_login_no_user(self):
        """
        Check that login returns 401 for user that is not in the database
        """
        print("TEST:test_login_no_user")
        response = self.client.post(
            '/api-token/', {'username': 'anonimo.alguien@unal.edu.co', 'password': 'contraseña'}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual('No active account found with the given credentials', response.json()['detail'])

    def test_login_incorrect_password(self):
        """
        Check that login returns 401 for incorrect password
        """
        print("TEST:test_login_incorrect_password")
        response = self.client.post(
            '/api-token/', {'username': 'santiago.garcia@unal.edu.co', 'password': 'contraseña'}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual('No active account found with the given credentials', response.json()['detail'])

    def test_login_incorrect_username(self):
        """
        Check that login returns 401 for incorrect username
        """
        print("TEST:test_login_incorrect_username")
        response = self.client.post(
            '/api-token/', {'username': 'santi.garcia@unal.edu.co', 'password': 'Password123'}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual('No active account found with the given credentials', response.json()['detail'])

    @classmethod
    def tearDownClass(cls):
        pass
