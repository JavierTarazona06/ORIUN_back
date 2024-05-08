import os
import student

from django.urls import reverse
from django.test import TestCase
from student.models import ContactPerson
from data.management.commands.populate_data import Command
from django.core.files.uploadedfile import SimpleUploadedFile

from call.models import Call
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        if Call.objects.count() == 0:
            command = Command()
            command.handle(path=os.path.join('data', 'data_csv'))

    def setUp(self):
        response = self.client.post(
            '/api-token/', {'username': 'maria.alvarez@unal.edu.co', 'password': 'Maria#1234'}
        )
        self.assertEqual(response.status_code, 200)
        self.token_employee = response.json()['access']

        response = self.client.post(
            '/api-token/', {'username': 'santiago.garcia@unal.edu.co', 'password': 'Password123'}
        )
        self.assertEqual(response.status_code, 200)
        self.token_student = response.json()['access']

    def test_authentication(self):
        """
        Current user must be authenticated and a student.
        """
        response = self.client.get(
            '/application/region_call/', {'call': 1}, headers={"Authorization": f"Bearer {self.token_employee}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['detail'], 'Current user is not a student')

    def test_region_call_uniandes(self):
        """
        Check that call 1 return Uniandes as region
        """
        response = self.client.get(
            '/application/region_call/', {'call': 1}, headers={"Authorization": f"Bearer {self.token_student}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['region'], 'Uniandes')

    # TODO: add national university to cvs and test
    def test_region_call_international(self):
        """
        Check that call 4 return Internacional as region
        """
        response = self.client.get(
            '/application/region_call/', {'call': 4}, headers={"Authorization": f"Bearer {self.token_student}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['region'], 'Internacional')

    def test_create_form_missing_info_contact(self):
        """
        Check that when given
        """
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
            "Authorization": f"Bearer {self.token_student}",
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
            "Authorization": f"Bearer {self.token_student}",
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
            "Authorization": f"Bearer {self.token_student}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        changed_contact_person = student.serializers.ContactPersonSerializer(ContactPerson.objects.get(id=1))
        self.assertEqual(changed_contact_person.data, contact_person)

    def test_create_form_missing_contact_person(self):
        """
        Check that when given
        """
        response = self.client.post(
            '/api-token/', {'username': 'valentina.rodriguez@unal.edu.co', 'password': 'TestPassword'}
        )
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
        data = {
            "diseases": 'de todo',
            "call": 4
        }
        headers = {
            "Authorization": f"Bearer {self.token_student}",
        }
        response = self.client.post(
            '/application/create_forms/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Forms filled successfully')

    def test_download_no_found(self):
        """

        """
        data = {
            "call": 5,
            "name_file": "request_form",
            "type_file": "filled_doc"
        }
        headers = {
            "Authorization": f"Bearer {self.token_student}",
        }
        response = self.client.get(
            '/application/download/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'form not found')

    def test_download_found(self):
        """

        """
        data = {
            "call": 4,
            "name_file": "request_form",
            "type_file": "filled_doc"
        }
        headers = {
            "Authorization": f"Bearer {self.token_student}",
        }
        response = self.client.get(
            '/application/download/', headers=headers, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'link')

    def test_upload_too_big(self):
        """

        """
        with open('data/big_file.mov', 'rb') as file:
            file_data = file.read()
            file_obj = SimpleUploadedFile('big_file.mov', file_data)
            headers = {
                "Authorization": f"Bearer {self.token_student}",
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
        with open('data/forms/templates/request_form.docx', 'rb') as file:
            file_data = file.read()
            file_obj = SimpleUploadedFile('request_form.docx', file_data)
            headers = {
                "Authorization": f"Bearer {self.token_student}",
            }
            data = {
                'name_file': 'request_form',
                'document': file_obj,
                'call': 2,
            }
            response = self.client.post('/application/upload/', data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'File uploaded successfully!')

    # case 10

    def test_application_doesnt_exist(self):
        """
           Returns a non-existent application error
        """
        print("TEST:test_application_doesnt_exist")

        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }

        response = self.client.get(reverse("application:applicants", args=[5]), headers=headers)

        self.assertEqual(response.status_code, 404)

    def test_get_applicants(self):
        """
        Return all applications with auth
        """

        print("TEST:test_get_applicants")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }
        response = self.client.get(reverse("application:applicants", args=[1]), headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_get_applicants_filter(self):
        """
        Return applications with filters allowed: student_id and state_documents
        """
        print("TEST:test_get_applicants_filter")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }

        data = {
            'student_id': 5596848490,
            'state_documents': 0
        }

        response = self.client.get(reverse("application:applicants", args=[1]), data=data, headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_request_modification(self):
        """
        Return state_document equal 1
        """
        print("TEST:test_request_modification")

        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }

        response = self.client.put(reverse("application:modify_application", args=[1, 5596848490]), headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['state_documents'], 1)

    def test_accept_documents(self):
        """
               Return state_document equal 2
               """
        print("TEST:test_accept_documents")

        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }

        response = self.client.put(reverse("application:accept_documents", args=[1,5596848490]), headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['state_documents'], 2)


    def test_make_comment(self):
        """
        Returns the message in which the comment was successfully added.
        """
        print("TEST:test_make_comment")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }

        data = {
            'comment': 'ola'
        }

        response = self.client.post(
            reverse("application:comment_application", args=[1,5596848490]), data=data, headers=headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], "Comment added successfully.")

    def test_status_documents_not_reviewed(self):
        """
                       Return state equal 0
                       """

        print("TEST:test_status_documents_not_reviewed")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }
        response = self.client.get(reverse("application:get_state", args=[1, 106985477]), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['state'], 0)

    def test_status_documents_request_modification(self):
        """
                               Return state equal 1
                               """

        print("TEST:test_status_documents_request_modification")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }

        response = self.client.get(reverse("application:get_state", args=[1, 1196989870]), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['state'], 1)

    def test_status_documents_accepted(self):
        """
                               Return state equal 2
                               """

        print("TEST:test_status_documents_accepted")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }
        response = self.client.get(reverse("application:get_state", args=[1, 5596848490]), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['state'], 2)

    def test_status_modified_by_student(self):
        """
                               Return state equal 3
                               """

        print("TEST:test_status_modified_by_student")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }
        response = self.client.get(reverse("application:get_state", args=[2, 1154658]), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['state'], 3)

    def test_get_documents(self):
        """
                               Return documents for a specifc application
                               """

        print("TEST:test_get_documents")
        headers = {
            "Authorization": f"Bearer {self.token_employee}",
        }
        response = self.client.get(reverse("application:documents_student", args=[1, 5596848490]), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_order_apps_by_docs(self):
        print("TEST: test_get_order_apps_by_docs")

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.get(reverse("application:order_apps_by_docs", args=[1]), headers=headers)

        qset = response.json()
        qsetr = [
            {'id': 1, 'student_id': '5596848490', 'student_name': 'Santiago García', 'state_documents': 2, 'student_PAPA': 4.8, 'student_advance': 92.0, 'student_headquarter': 'BO', 'language': True, 'student_PBM': 2},
            {'id': 2, 'student_id': '1196989870', 'student_name': 'Valentina Rodríguez', 'state_documents': 1, 'student_PAPA': 4.8, 'student_advance': 86.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 9},
            {'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def test_get_order_apps_by_papa(self):
        print("TEST: test_get_order_apps_by_papa")

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.get(reverse("application:order_apps_by_papa", args=[1]), headers=headers)

        qset = response.json()
        qsetr = [
            {'id': 1, 'student_id': '5596848490', 'student_name': 'Santiago García', 'state_documents': 2, 'student_PAPA': 4.8, 'student_advance': 92.0, 'student_headquarter': 'BO', 'language': True, 'student_PBM': 2},
            {'id': 2, 'student_id': '1196989870', 'student_name': 'Valentina Rodríguez', 'state_documents': 1, 'student_PAPA': 4.8, 'student_advance': 86.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 9},
            {'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def test_get_order_apps_by_advance(self):
        print("TEST: test_get_order_apps_by_advance")

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.get(reverse("application:order_apps_by_advance", args=[1]), headers=headers)

        qset = response.json()
        qsetr = [
            {'id': 1, 'student_id': '5596848490', 'student_name': 'Santiago García', 'state_documents': 2, 'student_PAPA': 4.8, 'student_advance': 92.0, 'student_headquarter': 'BO', 'language': True, 'student_PBM': 2},
            {'id': 2, 'student_id': '1196989870', 'student_name': 'Valentina Rodríguez', 'state_documents': 1, 'student_PAPA': 4.8, 'student_advance': 86.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 9},
            {'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def test_get_order_apps_by_language(self):
        print("TEST: test_get_order_apps_by_language")

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.get(reverse("application:order_apps_by_language", args=[1]), headers=headers)

        qset = response.json()
        qsetr = [
            {'id': 1, 'student_id': '5596848490', 'student_name': 'Santiago García', 'state_documents': 2, 'student_PAPA': 4.8, 'student_advance': 92.0, 'student_headquarter': 'BO', 'language': True, 'student_PBM': 2},
            {'id': 2, 'student_id': '1196989870', 'student_name': 'Valentina Rodríguez', 'state_documents': 1, 'student_PAPA': 4.8, 'student_advance': 86.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 9},
            {'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def test_get_order_apps_by_pbm(self):
        print("TEST: test_get_order_apps_by_pbm")

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.get(reverse("application:order_apps_by_pbm", args=[1]), headers=headers)

        qset = response.json()
        qsetr = [
            {'id': 1, 'student_id': '5596848490', 'student_name': 'Santiago García', 'state_documents': 2, 'student_PAPA': 4.8, 'student_advance': 92.0, 'student_headquarter': 'BO', 'language': True, 'student_PBM': 2},
            {'id': 2, 'student_id': '1196989870', 'student_name': 'Valentina Rodríguez', 'state_documents': 1, 'student_PAPA': 4.8, 'student_advance': 86.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 9},
            {'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def test_get_order_apps_general(self):
        print("TEST: test_get_order_apps_general")

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.get(reverse("application:order_apps_general", args=[1]), headers=headers)

        qset = response.json()
        qsetr = [
            {'id': 1, 'student_id': '5596848490', 'student_name': 'Santiago García', 'state_documents': 2, 'student_PAPA': 4.8, 'student_advance': 92.0, 'student_headquarter': 'BO', 'language': True, 'student_PBM': 2},
            {'id': 2, 'student_id': '1196989870', 'student_name': 'Valentina Rodríguez', 'state_documents': 1, 'student_PAPA': 4.8, 'student_advance': 86.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 9},
            {'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)

    def test_set_winner(self):
        print("TEST: test_set_winner")

        data = {
            "application_id": 1,
            "student_id": 5596848490
        }

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.post(reverse("application:set_winner"), data=data, headers=headers)

        qset = Application.objects.filter(id=data['application_id'], student_id=data['student_id'])
        qset = ApplicationSerializer(qset, many=True).data[0]
        qsetr = {
            'id': 1,
            'year': 2024,
            'semester': '1',
            'is_extension': False,
            'comment': None,
            'state_documents': 2,
            'modified': False,
            'approved': True,
            'training_session': None,
            'call': 1, 'student': 5596848490}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)
        self.assertEqual(response.json(), {"mesage":f"El estudiante con ID {data["student_id"]} fue seleccionado para la convocatoria {qset["call"]}"})

    def test_not_winner(self):
        print("TEST: test_not_winner")

        data = {
            "application_id": 1,
            "student_id": 5596848490
        }

        headers = {"Authorization": f"Bearer {self.token_employee}"}
        response = self.client.post(reverse("application:not_winner"), data=data, headers=headers)

        qset = Application.objects.filter(id=data['application_id'], student_id=data['student_id'])
        qset = ApplicationSerializer(qset, many=True).data[0]
        qsetr = {
            'id': 1,
            'year': 2024,
            'semester': '1',
            'is_extension': False,
            'comment': None,
            'state_documents': 2,
            'modified': False,
            'approved': False,
            'training_session': None,
            'call': 1, 'student': 5596848490}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(qset, qsetr)
        self.assertEqual(response.json(), {"mesage":f"El estudiante con ID {data["student_id"]} fue des-seleccionado para la convocatoria {qset["call"]}"})

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
