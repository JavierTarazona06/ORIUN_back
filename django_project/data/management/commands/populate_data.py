from django.core.management.base import BaseCommand
from call.models import Call, University
from student.models import ContactPerson, Student
from employee.models import Employee
import pandas as pd
import os
from django.contrib.auth.models import User
from datetime import datetime




class Command(BaseCommand):
    help = 'Populate University, Call, Student models from CSV'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default='data_csv',
                            help='Path to the CSV folder')

    def handle(self, *args, **options):
        csv_folder = options['path']
        #obtainng aboslute paht folder
        csv_abs_path = os.path.abspath(csv_folder)


        university_csv_path = os.path.join(csv_abs_path, 'university_data.csv')
        if not os.path.exists(university_csv_path):
            self.stdout.write(self.style.WARNING(f"University data file '{university_csv_path}' does not exist."))
            return

        university_df = pd.read_csv(university_csv_path, delimiter=';')
        universities = {}
        for index, row in university_df.iterrows():
            university = University.objects.create(
                name=row['name'],
                webpage=row['webpage'],
                region=row['region'],
                country=row['country'],
                city=row['city'],
                academic_offer=row['academic_offer'],
                exchange_info=row['exchange_info']
            )
            universities[university.id] = university
        self.stdout.write(self.style.SUCCESS(f"Populated {len(universities)} universities."))

        # Populating data to call table
        call_csv_path = os.path.join(csv_abs_path, 'call_data.csv')
        if not os.path.exists(call_csv_path):
            self.stdout.write(self.style.WARNING(f"Call data file '{call_csv_path}' does not exist."))
            return

        call_df = pd.read_csv(call_csv_path, delimiter=';')
        for index, row in call_df.iterrows():
            university_id = row['university_id']
            university = universities.get(university_id)
            if university:
                Call.objects.create(
                    university_id=university,
                    active=row['active'],
                    begin_date=row['begin_date'],
                    deadline=row['deadline'],
                    min_advance=row['min_advance'],
                    min_papa=row['min_papa'],
                    format=row['format'],
                    study_level=row['study_level'],
                    year=row['year'],
                    semester=row['semester'],
                    language=row['language'],
                    description=row['description'],
                    available_slots=row['available_slots'],
                    note=row['note'],
                    highest_papa_winner=row['highest_papa_winner'],
                    minimum_papa_winner=row['minimum_papa_winner'],
                    selected=row['selected']
                )
        self.stdout.write(self.style.SUCCESS(f"Populated {len(call_df)} calls."))

        # Populating data to student table
        student_csv_path = os.path.join(csv_abs_path, 'student_data.csv')
        if not os.path.exists(student_csv_path):
            self.stdout.write(self.style.WARNING(f"Student data file '{student_csv_path}' does not exist."))
            return
        
        student_df = pd.read_csv(student_csv_path, delimiter=';')
        for index, row in student_df.iterrows():
            birth_date = datetime.strptime(str(row['birth']), '%Y-%m-%d').date()

            user = User.objects.create_user(
                username=row['username'],
                password=str(row['password']),
                email=str(row['email'])
            )

            # Create a student associated with the user

            student = Student.objects.create(
                user=user,
                type_user=row['type_user'],
                type_document=row['type_document'],
                name=row['name'],
                lastname=row['lastname'],
                birth=birth_date,
                sex=row['sex'],
                country=row['country'],
                city=row['city'],
                phone=row['phone'],
                address=row['address'],
                ethnicity=row['ethnicity'],
                headquarter=row['headquarter'],
                PAPA=row['PAPA'],
                PAPI=row['PAPI'],
                PA=row['PA'],
                PBM=row['PBM'],
                advance=row['advance'],
                faculty=row['faculty'],
                major=row['major'],
                is_enrolled=row['is_enrolled'],
                #date_banned_mobility=row['date_banned_mobility'],
                is_banned_behave_un=row['is_banned_behave_un'],
                admission=row['admission'],
                study_level=row['study_level'],
                num_semesters=row['num_semesters'],
                #contact_id = row['contact_id']
            )


        self.stdout.write(self.style.SUCCESS(f"Populated {len(student_df)} students."))


        # Populating data to employee table
        employee_csv_path = os.path.join(csv_abs_path, 'employee_data.csv')
        if not os.path.exists(employee_csv_path):
            self.stdout.write(self.style.WARNING(f"Employee data file '{employee_csv_path}' does not exist."))
            return

        employee_df = pd.read_csv(employee_csv_path, delimiter=';')
        for index, row in employee_df.iterrows():
            birth_date = datetime.strptime(str(row['birth']), '%Y-%m-%d').date()

            user = User.objects.create_user(
                username=row['username'],
                password=str(row['password']),
                email=str(row['email'])
            )
            # Create an employee associated with the user
            employee = Employee.objects.create(
                user=user,
                type_user=row['type_user'],
                type_document=row['type_document'],
                name=row['name'],
                lastname=row['lastname'],
                birth=birth_date,
                sex=row['sex'],
                birth_place=row['birth_place'],
                country=row['country'],
                city=row['city'],
                phone=row['phone'],
                address=row['address'],
                ethnicity=row['ethnicity'],
                headquarter=row['headquarter'],
                dependency=row['dependency']
            )

        self.stdout.write(self.style.SUCCESS(f"Populated {len(student_df)} employees."))

