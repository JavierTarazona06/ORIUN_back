from django.core.management.base import BaseCommand
from call.models import Call, University
import pandas as pd


class Command(BaseCommand):
    help = 'Populate University and Call models from CSV'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default='/Users/knsmolina.28/Desktop/data',
                            help='Path to the CSV folder')

    def handle(self, *args, **options):
        csv_folder = options['path']

        university_csv_path = f"{csv_folder}/university_data.csv"
        university_df = pd.read_csv(university_csv_path, delimiter=';')
        for index, row in university_df.iterrows():
            region = row['region']
            language = row['language'].split(',') if row['language'] else []
            university = University.objects.create(
                name=row['name'],
                webpage=row['webpage'],
                region=region,
                country=row['country'],
                city=row['city'],
                language=language,
                academic_offer=row['academic_offer'],
                exchange_info=row['exchange_info']
            )

        # Fill the model Call from  call_data.csv
        call_csv_path = f"{csv_folder}/call_data.csv"
        call_df = pd.read_csv(call_csv_path, delimiter=';')
        for index, row in call_df.iterrows():
            university_name = row['university_name']
            university = University.objects.get(name=university_name)
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
                note=row['note']
            )
