import os
import csv
from employee.models import Employee
from datetime import datetime, timezone
from call.models import Call, University
from application.models import Application
from django.contrib.auth.models import User
from application.helpers import upload_object
from student.models import Student, ContactPerson
from django.core.management.base import BaseCommand
from application.serializers import ApplicationSerializer


class Command(BaseCommand):
    help = 'Populate University, Call, Contact Person, Student, Employee and Applications models from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default='data/data_csv', help='Path to the CSV folder')
        parser.add_argument('--upload', type=bool, default=False, help='Whether or not upload the docs to GCP')

    def open_csv(self, csv_abs_path, name_file):
        path_file = os.path.join(csv_abs_path, name_file)
        if not os.path.exists(path_file):
            self.stdout.write(self.style.WARNING(f"File '{path_file}' does not exist."))
            return

        with open(path_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=',')
            info = list()
            for row in reader:
                for name, value in row.items():
                    if value == '':
                        row[name] = None
                info.append(row)

        return info

    def populate_user(self, csv_abs_path, type_user):
        """
        Populates student or employee model. type_user can be 'student' or 'employee'
        """
        data = self.open_csv(csv_abs_path, f'{type_user}_data.csv')
        for info in data:
            user = User.objects.create_user(
                username=info['username'],
                password=info['password'],
                first_name=info['first_name'],
                last_name=info['last_name'],
                email=info['email']
            )
            info['user'] = user
            del info['username']
            del info['password']
            del info['email']
            del info['first_name']
            del info['last_name']
            info['birth_date'] = datetime.strptime(info['birth_date'], '%Y-%m-%d').date()

            if type_user == 'student':
                if info['contact_person'] is not None:
                    info['contact_person'] = ContactPerson.objects.get(id=info['contact_person'])
                Student.objects.create(**info)
            else:
                Employee.objects.create(**info)
        self.stdout.write(self.style.SUCCESS(f"Populated {len(data)} {type_user}s."))

    def upload_docs(self, student_id, call_id):
        """
        Uploads documents (only general ones) to GCP in order to create an application for a student
        """
        base_docs = Application.name_docs
        call = Call.objects.get(id=call_id)
        region = call.university_id.get_region_display()
        if region == 'Uniandes':
            pass
        elif region == 'Convenio Sigueme/Nacional':
            base_docs.extend(Application.national_name_docs)
        else:
            base_docs.extend(Application.international_name_docs)

        path = os.path.join('data', 'docs_applications', 'general')
        for doc in os.listdir(path):
            if doc.split('.')[0] in base_docs:
                with open(os.path.join(path, doc), 'rb') as f:
                    name_file, extension = doc.split('.')
                    name = f'{name_file}_{student_id}_{call_id}.{extension}'
                    upload_object('complete_doc', f, name)

    def handle(self, *args, **options):
        csv_folder = options['path']
        csv_abs_path = os.path.abspath(csv_folder)

        # Populate universities
        data_universities = self.open_csv(csv_abs_path, 'university_data.csv')
        for info in data_universities:
            University.objects.create(**info)
        self.stdout.write(self.style.SUCCESS(f"Populated {len(data_universities)} universities."))

        # Populate calls
        data_calls = self.open_csv(csv_abs_path, 'call_data.csv')
        for info in data_calls:
            info['university_id'] = University.objects.get(id=info['university_id'])
            Call.objects.create(**info)
        self.stdout.write(self.style.SUCCESS(f"Populated {len(data_calls)} calls."))

        # Populate contact person
        data_contact_person = self.open_csv(csv_abs_path, 'contact_person_data.csv')
        for info in data_contact_person:
            ContactPerson.objects.create(**info)
        self.stdout.write(self.style.SUCCESS(f"Populated {len(data_contact_person)} contact people."))

        # Populate student
        self.populate_user(csv_abs_path, 'student')

        # Populate employee
        self.populate_user(csv_abs_path, 'employee')

        # Populate applications
        data_applications = self.open_csv(csv_abs_path, 'applications_data.csv')
        upload = options.get('upload')

        for info in data_applications:
            if upload:
                self.upload_docs(info['student'], info['call'])
            info['year'], month = datetime.now(timezone.utc).strftime('%Y %m').split(" ")
            info['semester'] = '1' if int(month) <= 6 else '2'
            s = ApplicationSerializer(data=info)
            s.is_valid(raise_exception=True)
            s.save()

        self.stdout.write(self.style.SUCCESS(f"Populated {len(data_applications)} applications."))

