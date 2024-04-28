import json

from django.test import TestCase
from django.urls import reverse
from call.models import Call, University
from employee.models import Employee
from data.management.commands.populate_data import Command
from call.serializers import CallSerializer, UniversitySerializer
from django.utils import timezone
from django.db.models import Q

import requests


class CallsTestCase2(TestCase):

    @classmethod
    def setUpClass(cls):
        # Populate DB
        comm = Command()
        comm.handle(path=r"C:\Users\javit\Documents\ORIUN_back\django_project\data\data_csv")

    def setUp(self):
        # User auth
        # cur_user = Employee.objects.get(user__username='maria_alvarez')
        response = self.client.post('/api-token/', {'username': 'maria_alvarez', 'password': 'Maria#1234'})
        self.assertEqual(response.status_code, 200)

        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token = response_body['access']

        response = self.client.post('/api-token/', {'username': 'santiago_garcia', 'password': 'Password123'})
        self.assertEqual(response.status_code, 200)

        response_body = json.loads(response.content.decode('utf-8'))
        self.bearer_token_std = response_body['access']

    # 1: Get Call: Employee
    def test_get_all_calls_noauth(self):
        """
        Return all calls without auth
        """
        print("TEST: test_get_all_calls_noauth")

        response = self.client.get(reverse("call:calls_list"))

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'Authentication credentials were not provided.'})

    def test_get_all_calls_wrong_auth(self):
        """
        Return all calls with wrong auth
        """
        print("TEST: test_get_all_calls_wrong_auth")

        authorization_header = {"HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"}
        response = self.client.get(reverse("call:calls_list"), **authorization_header)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_get_all_calls(self):
        """
        Return all calls with
        """
        print("TEST: test_get_all_calls_auth")

        authorization_header = {"HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"}
        response = self.client.get(reverse("call:calls_list"), **authorization_header)

        queryset = Call.objects.all()
        serializer = CallSerializer(queryset, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)

    # 2: Post Call: Employee

    def test_post_call_noauth(self):
        print("TEST: test_post_call_noauth")

        data = {
            "format": "V",
            "study_level": "PRE",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {}

        response = self.client.post(reverse("call:calls_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'Authentication credentials were not provided.'})

    def test_post_call_wrongauth(self):
        print("TEST: test_post_call_wrongauth")

        data = {
            "format": "V",
            "study_level": "PRE",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.bearer_token_std}"
        }

        response = self.client.post(reverse("call:calls_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_post_call(self):
        print("TEST: test_post_call")

        data = {
            "format": "V",
            "study_level": "PRE",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.bearer_token}"
        }

        response = self.client.post(reverse("call:calls_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['mensaje'], 'Convocatoria creada exitosamente')

    # 3. Get Call by ID: Employee

    def test_get_call_wrgauth(self):
        """
        Return call with given id wrong auth
        """
        print("TEST: test_get_call_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:calls_detail", args=[2]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_get_call(self):
        """
        Return call with given id
        """
        print("TEST: test_get_call")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_detail", args=[2]), **headers)

        queryset = Call.objects.get(pk=2)
        serializer = CallSerializer(queryset, many=False)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)

    # 4. Update Call: Employee

    def test_put_call(self):
        print("TEST: test_put_call")

        queryset = Call.objects.get(pk=2)
        serializer = CallSerializer(queryset, many=False)
        study_level1 = serializer.data['study_level']

        data = {
            "format": "V",
            "study_level": "POS",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.put(reverse("call:calls_update_by_id", args=[2]), data=data,
                                   content_type='application/json', **headers)

        queryset = Call.objects.get(pk=2)
        serializer = CallSerializer(queryset, many=False)
        study_level2 = serializer.data['study_level']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"mensaje": "Convocatoria actualizada exitosamente"})
        self.assertNotEqual(study_level1, study_level2)
        self.assertEqual("Postgrado", study_level2)

    def test_put_no_call(self):
        print("TEST: test_put_no_call")

        data = {
            "format": "V",
            "study_level": "POS",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 1
        }

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.put(reverse("call:calls_update_by_id", args=[15]), data=data,
                                   content_type='application/json', **headers)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'La convocatoria especificada no existe'})

    def test_put_call_no_uni(self):
        print("TEST: test_put_call_no_uni")

        data = {
            "format": "V",
            "study_level": "POS",
            "language": "en",
            "active": False,
            "begin_date": "2023-04-25",
            "deadline": "2023-06-20",
            "min_advance": 25,
            "min_papa": 3.5,
            "year": 2025,
            "semester": "1",
            "description": "NEW new Participar en un programa de intercambio estudiantil en la Universidad de Ulsan. Para más información sobre los programas de intercambio, visita el siguiente enlace: https://www.ulsan.ac.kr/.",
            "available_slots": 15,
            "note": None,
            "highest_papa_winner": 4.6,
            "minimum_papa_winner": 4.2,
            "selected": 15,
            "university": 15
        }

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.put(reverse("call:calls_update_by_id", args=[2]), data=data,
                                   content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'La universidad especificada no existe'})

    # 5. Delete Call: Employee

    def test_delete_nocall(self):
        print("TEST: test_delete_nocall")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.delete(reverse("call:calls_detail", args=[0]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"error": "No Call matches the given query."})

    def test_delete_call(self):
        print("TEST: test_delete_call")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.delete(reverse("call:calls_detail", args=[8]), **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensaje': 'Convocatoria eliminada satisfactoriamente'})

        err = ''
        try:
            cur_call = Call.objects.get(id=8)
        except Exception as e:
            err = str(e)

        self.assertEqual(err, 'Call matching query does not exist.')

    def test_delete_call_wrgauth(self):
        print("TEST: test_delete_call_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.delete(reverse("call:calls_detail", args=[8]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    # 6. Open Calls: Employee
    def test_open_calls(self):
        print("TEST: test_open_calls")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_opened"), **headers)

        current_date = timezone.now().date()
        qset = Call.objects.filter(deadline__gte=current_date, active=True)
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_open_calls_wrgauth(self):
        print("TEST: test_open_callswrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:calls_opened"), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    # 7. Closed Calls: Employee

    def test_closed_calls(self):
        print("TEST: test_closed_calls")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_closed"), **headers)

        current_date = timezone.now().date()
        qset = Call.objects.filter(Q(deadline__lt=current_date) | Q(active=False))
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_closed_calls_wrgauth(self):
        print("TEST: test_closed_callswrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:calls_closed"), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    # 8. Filter Over Calls: Employee

    def test_filter_calls_wrgauth(self):
        print("TEST: test_filter_calls_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:calls_employee_filter"), **headers)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {'detail': 'You do not have permission to perform this action.'})

    def test_filter_calls(self):
        print("TEST: test_filter_calls")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter"), **headers)

        qset = Call.objects.all()
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_id(self):
        print("TEST: test_filter_calls_id")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?call_id=2", **headers)

        qset = Call.objects.filter(id=2)
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_active(self):
        print("TEST: test_filter_calls_active")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?active=True", **headers)

        qset = Call.objects.filter(active=True)
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_format(self):
        print("TEST: test_filter_calls_format")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?formato=P", **headers)

        qset = Call.objects.filter(format="P")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_study_level(self):
        print("TEST: test_filter_calls_study_level")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?study_level=PRE", **headers)

        qset = Call.objects.filter(study_level="PRE")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_language(self):
        print("TEST: test_filter_calls_language")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?language=en", **headers)

        qset = Call.objects.filter(language="en")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_deadline(self):
        print("TEST: test_filter_calls_deadline")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?deadline=2024-05-15", **headers)

        qset = Call.objects.filter(deadline__lte="2024-05-15")
        qset = qset.filter(deadline__gte=timezone.now().date())
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_university_id(self):
        print("TEST: test_filter_calls_university_id")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?university_id=3", **headers)

        qset = Call.objects.filter(university__id=3)
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_university_name(self):
        print("TEST: test_filter_calls_university_name")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?university_name=Politecnico di Milano",
                                   **headers)

        qset = Call.objects.filter(university__name="Politecnico di Milano")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_year(self):
        print("TEST: test_filter_calls_year")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?year=2024", **headers)

        qset = Call.objects.filter(year="2024")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_semester(self):
        print("TEST: test_filter_calls_semester")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?semester=2", **headers)

        qset = Call.objects.filter(semester="2")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_region(self):
        print("TEST: test_filter_calls_region")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?region=NA", **headers)

        qset = Call.objects.filter(university__region="NA")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_country(self):
        print("TEST: test_filter_calls_country")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?country=Italia", **headers)

        qset = Call.objects.filter(university__country__icontains="Italia")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    def test_filter_calls_lang_and_year(self):
        print("TEST: test_filter_calls_lang_and_year")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:calls_employee_filter") + "?language=es&year=2024", **headers)

        qset = Call.objects.filter(year="2024")
        qset = qset.filter(language="es")
        qset = CallSerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    # 9. Get Universities: Employee

    def test_get_universities_wrgauth(self):
        print("TEST: test_get_universities_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:univ_list"), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_get_universities(self):
        print("TEST: test_get_universities")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:univ_list"), **headers)

        qset = University.objects.all()
        qset = UniversitySerializer(qset, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    # 10. Create Universities: Employee

    def test_post_universities_wrgauth(self):
        print("TEST: test_post_universities_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        data = {
            "region": "LA",
            "name": "Universidad de Mexico",
            "webpage": "https://unam.mx/",
            "country": "Mexico",
            "city": "Ciudad de Mexico",
            "academic_offer": "https://oferta.unam.mx/",
            "exchange_info": "https://oferta.unam.mx/"
        }

        response = self.client.post(reverse("call:univ_list"), data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_post_universities(self):
        print("TEST: test_post_universities")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        data = {
            "region": "LA",
            "name": "Universidad de Mexico",
            "webpage": "https://unam.mx/",
            "country": "Mexico",
            "city": "Ciudad de Mexico",
            "academic_offer": "https://oferta.unam.mx/",
            "exchange_info": "https://oferta.unam.mx/"
        }

        response = self.client.post(reverse("call:univ_list"), data=data, content_type='application/json', **headers)

        qset = University.objects.filter(pk=8)
        qset = UniversitySerializer(qset, many=True).data

        data["id"] = 8
        data["region"] = "Latinoamérica"
        ldata = [data]

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensaje': 'Universidad creada exitosamente', 'id': 8})
        self.assertEqual(qset, ldata)

    # 11. Get University by ID: Employee

    def test_get_university_id_wrgauth(self):
        print("TEST: test_get_university_id_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.get(reverse("call:univ_detail", args=[2]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_get_university_id(self):
        print("TEST: test_get_university_id")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.get(reverse("call:univ_detail", args=[2]), **headers)

        qset = University.objects.filter(pk=2)
        qset = UniversitySerializer(qset, many=True).data[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), qset)

    # 12.  Update Universities: Employee

    def test_put_university(self):
        print("TEST: test_put_university")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        data0 = University.objects.filter(pk=1)
        data0 = UniversitySerializer(data0, many=True).data[0]

        data_f = {
            "region": "LA",
            "name": "Universidad de los Andes y mas",
            "webpage": "https://uniandes.edu.co/ca",
            "country": "Colombiano",
            "city": "Bogotáno",
            "academic_offer": "Ahttps://aspirantes.uniandes.edu.co/es/aspirantes-internacionales",
            "exchange_info": "Ahttps://aspirantes.uniandes.edu.co/es/aspirantes-internacionales"
        }

        response = self.client.put(reverse("call:University_update_by_id", args=[1]), data=data_f,  content_type='application/json', **headers)

        qset = University.objects.filter(pk=1)
        qset = UniversitySerializer(qset, many=True).data[0]

        data_f["id"] = 1
        data_f["region"] = "Latinoamérica"
        ldata = data_f

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensaje': 'Universidad actualizada exitosamente'})
        self.assertNotEqual(data0, qset)
        self.assertEqual(ldata, qset)

        data_t = {
            "region": "AN",
            "name": "Universidad de los Andes",
            "webpage": "https://uniandes.edu.co/",
            "country": "Colombia",
            "city": "Bogotá",
            "academic_offer": "https://aspirantes.uniandes.edu.co/es/aspirantes-internacionales",
            "exchange_info": "https://aspirantes.uniandes.edu.co/es/aspirantes-internacionales"
        }

        _response = self.client.put(reverse("call:University_update_by_id", args=[1]), data=data_t,  content_type='application/json', **headers)

        qset = University.objects.filter(pk=1)
        qset = UniversitySerializer(qset, many=True).data[0]

        self.assertEqual(data0, qset)

    # 13.  Delete Universities: Employee

    def test_delete_university_wrgauth(self):
        print("TEST: test_delete_university_wrgauth")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token_std}"
        }

        response = self.client.delete(reverse("call:univ_detail", args=[7]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'You do not have permission to perform this action.'})

    def test_delete_university_no_uni(self):
        print("TEST: test_delete_university_no_uni")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.delete(reverse("call:univ_detail", args=[8]), **headers)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'No University matches the given query.'})

    def test_delete_university(self):
        print("TEST: test_delete_university")

        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.bearer_token}"
        }

        response = self.client.delete(reverse("call:univ_detail", args=[7]), **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensaje': 'Universidad eliminada satisfactoriamente'})

        err = ''
        try:
            cur_uni = University.objects.get(id=7)
        except Exception as e:
            err = str(e)

        self.assertEqual(err, 'University matching query does not exist.')


    @classmethod
    def tearDownClass(cls):
        pass
