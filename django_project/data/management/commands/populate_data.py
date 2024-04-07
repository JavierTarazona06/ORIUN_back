from django.core.management.base import BaseCommand
from person.models import Person
from call.models import Call, University
from student.models import ContactPerson, Student
import pandas as pd


class Command(BaseCommand):
    help = 'Populate University,Call models from CSV'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default='data',
                            help='Path to the CSV folder')

    def handle(self, *args, **options):
        csv_folder = options['path']

#Populate data  to university table
        university_csv_path = f"{csv_folder}/university_data.csv"
        university_df = pd.read_csv(university_csv_path, delimiter=';')
        universities = {}
        for index, row in university_df.iterrows():
            language = [lang.strip() for lang in row['language'].strip('[]').split(',')] if row['language'] else []
            university = University.objects.create(
                name=row['name'],
                webpage=row['webpage'],
                region=row['region'],
                country=row['country'],
                city=row['city'],
                language=language,
                academic_offer=row['academic_offer'],
                exchange_info=row['exchange_info']
            )
            universities[university.id] = university
        print(universities)

#Populating data to call table
        call_csv_path = f"{csv_folder}/call_data.csv"
        call_df = pd.read_csv(call_csv_path, delimiter=';')
        for index, row in call_df.iterrows():
            university_id = row['university_id']
            university = universities[university_id]
            call = Call.objects.create(
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
                description=row['description'],
                available_slots=row['available_slots'],
                note=row['note'],
                highest_papa_winner = row['highest_papa_winner'],
                minimum_papa_winner=row['minimum_papa_winner'],
                selected = row['selected']
            )
