from django.core.management.base import BaseCommand
from person.models import Person
from call.models import Call, University
from student.models import ContactPerson, Student
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Populate University, Call models from CSV'

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
