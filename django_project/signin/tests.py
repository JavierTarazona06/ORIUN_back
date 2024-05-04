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
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'refresh')
        self.assertContains(response, 'access')
        self.assertContains(response, 'type_user')
        self.assertEqual(response.json()['type_user'], 'student')

    def test_login_employee(self):
        """
        Checks that login returns 2 tokens (refresh and access) and type_user is employee
        """
        response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'refresh')
        self.assertContains(response, 'access')
        self.assertContains(response, 'type_user')
        self.assertEqual(response.json()['type_user'], 'employee')

    def test_login_no_user(self):
        """
        Check that login returns 401 for user that is not in the database
        """
        response = self.client.post('/api-token/', {'username': 'anonimo', 'password': 'contraseña'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual('No active account found with the given credentials', response.json()['detail'])

    def test_login_incorrect_password(self):
        """
        Check that login returns 401 for incorrect password
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'contraseña'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual('No active account found with the given credentials', response.json()['detail'])

    def test_login_incorrect_username(self):
        """
        Check that login returns 401 for incorrect username
        """
        response = self.client.post('/api-token/', {'username': 'santiago', 'password': 'Password123'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual('No active account found with the given credentials', response.json()['detail'])

    @classmethod
    def tearDownClass(cls):
        pass
