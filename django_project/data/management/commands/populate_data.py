import os
import csv
from datetime import datetime
from student.models import Student
from employee.models import Employee
from call.models import Call, University
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate University, Call, Student models from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default='data/data_csv', help='Path to the CSV folder')

    def open_csv(self, csv_abs_path, name_file):
        path_file = os.path.join(csv_abs_path, name_file)
        if not os.path.exists(path_file):
            self.stdout.write(self.style.WARNING(f"File '{path_file}' does not exist."))
            return

        with open(path_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
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
                Student.objects.create(**info)
            else:
                Employee.objects.create(**info)
        self.stdout.write(self.style.SUCCESS(f"Populated {len(data)} {type_user}s."))

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
            info['university'] = University.objects.get(id=info['university'])
            Call.objects.create(**info)
        self.stdout.write(self.style.SUCCESS(f"Populated {len(data_calls)} calls."))

        # Populate student
        self.populate_user(csv_abs_path, 'student')

        # Populate employee
        self.populate_user(csv_abs_path, 'employee')

        # TODO: Populate applications
