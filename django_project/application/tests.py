import os
import student
from call.models import Call
from django.test import TestCase
from student.models import ContactPerson
from data.management.commands.populate_data import Command


class ApplicationTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        if Call.objects.count() == 0:
            command = Command()
            command.handle(path=os.path.join('data', 'data_csv'))

    def test_authentication(self):
        """
        Current user must be authenticated and a student.
        """
        response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
        response = self.client.get(
            '/application/region_call/', {'call': 1}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['detail'], 'Current user is not a student')

    def test_region_call_uniandes(self):
        """
        Check that call 1 return Uniandes as region
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        response = self.client.get(
            '/application/region_call/', {'call': 1}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['region'], 'Uniandes')

    # TODO: add national university to cvs and test
    def test_region_call_international(self):
        """
        Check that call 4 return Internacional as region
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        response = self.client.get(
            '/application/region_call/', {'call': 4}, headers={"Authorization": f"Bearer {response.json()['access']}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['region'], 'Internacional')

    def test_create_form_missing_info_contact(self):
        """
        Check that when given
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        data = {
            "contact_person": {
                "name": "nombre",
                "relationship": "relacion",
                "cellphone": "123456789",
                "email": "correo@correo.com"
            },
            "call": 4
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['contact_person']['last_name'][0], 'This field is required.')

    def test_create_form_incorrect_info_contact(self):
        """
        Check that when given
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        data = {
            "contact_person": {
                "name": "nombre",
                "last_name": "appelido",
                "relationship": "relacion",
                "cellphone": "123456789",
                "email": "correo@"
            },
            "call": 4
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['contact_person']['email'][0], 'Enter a valid email address.')

    def test_create_form_correct_info_contact(self):
        """
        Check that when given
        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        contact_person = {
                "id": 1,
                "name": "Jonathan",
                "last_name": "appelido",
                "relationship": "relacion",
                "cellphone": "123456789",
                "email": "correo@email.com"
            }
        data = {
            "contact_person": contact_person,
            "call": 4
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        changed_contact_person = student.serializers.ContactPersonSerializer(ContactPerson.objects.get(id=1))
        self.assertEquals(changed_contact_person.data, contact_person)

    def test_create_form_missing_contact_person(self):
        """
        Check that when given
        """
        response = self.client.post('/api-token/', {'username': 'valentina_rodriguez', 'password': 'TestPassword'})
        data = {
            "call": 4
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'La persona de contacto no ha sido definida')

    def test_create_form_correct(self):
        """

        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        data = {
            "diseases": 'de todo',
            "call": 4
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.json()['message'], 'Forms filled successfully')

    def test_download_no_found(self):
        """

        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        data = {
            "call": 5,
            "name_file": "request_form",
            "type_file": "filled_doc"
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.get(
            '/application/download/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertEquals(response.json()['message'], 'form not found')

    def test_download_found(self):
        """

        """
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        data = {
            "call": 4,
            "name_file": "request_form",
            "type_file": "filled_doc"
        }
        headers = {
            "Authorization": f"Bearer {response.json()['access']}",
        }
        response = self.client.get(
            '/application/download/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'link')

    def test_upload_too_big(self):
        """

        """
        from django.core.files.uploadedfile import SimpleUploadedFile
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})

        with open('/home/valeria/Downloads/videos infracom/10 WLAN 02.mov', 'rb') as file:
            file_data = file.read()
            file_obj = SimpleUploadedFile('10 WLAN 02.mov', file_data)
            headers = {
                "Authorization": f"Bearer {response.json()['access']}",
            }
            data = {
                'name_file': 'grades_certificate',
                'document': file_obj,
                'call': 5,
            }

            response = self.client.post('/application/upload/', data=data, headers=headers)
        self.assertEqual(response.status_code, 413)
        self.assertEqual(response.json()['error'], 'File is too big. It must be smaller than 9 MB')

    def test_upload_correct(self):
        """

        """
        from django.core.files.uploadedfile import SimpleUploadedFile
        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})

        with open('data/forms/templates/request_form.docx', 'rb') as file:
            file_data = file.read()
            file_obj = SimpleUploadedFile('request_form.docx', file_data)
            headers = {
                "Authorization": f"Bearer {response.json()['access']}",
            }
            data = {
                'name_file': 'request_form',
                'document': file_obj,
                'call': 2,
            }
            response = self.client.post('/application/upload/', data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'File uploaded successfully!')

    @classmethod
    def tearDownClass(cls):
        pass
