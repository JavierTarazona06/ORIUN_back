from django.core.management.base import BaseCommand
from student.models import Student
from call.models import Call, University
from application.models import Application
from employee.models import Employee
import pandas as pd

class Command(BaseCommand):
    help = 'Populate University model from CSV'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default='/Users/knsmolina.28/Desktop/data', help='Path to the CSV folder')

    def handle(self, *args, **options):
        csv_path = options['path']
        df = pd.read_csv(csv_path+'/university_data.csv', delimiter=';')
        for index, row in df.iterrows():
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

        
