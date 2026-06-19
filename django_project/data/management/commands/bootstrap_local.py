import os
from datetime import date

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand

from call.models import Call
from employee.models import Employee
from student.models import ContactPerson, Student


class Command(BaseCommand):
    help = "Seed a local, reproducible ORIUN environment for Docker users."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="data/data_csv",
            help="Path to the CSV folder used for base demo data.",
        )

    def ensure_user(self, username, password, first_name, last_name, *, is_staff=False, is_superuser=False):
        user, _ = User.objects.get_or_create(username=username)
        user.email = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save()
        return user

    def ensure_guest_student(self):
        contact, _ = ContactPerson.objects.update_or_create(
            email="guest.contact@oriun.local",
            defaults={
                "name": "Guest",
                "last_name": "Contact",
                "relationship": "Emergency contact",
                "cellphone": "3001234567",
            },
        )
        user = self.ensure_user(
            "guest.student@unal.edu.co",
            "GuestStudent123!",
            "Guest",
            "Student",
        )
        Student.objects.update_or_create(
            id=900000001,
            defaults={
                "user": user,
                "birth_place": "Bogota",
                "country": "Colombia",
                "city": "Bogota",
                "phone": "3001234567",
                "address": "Local demo address",
                "birth_date": date(2000, 1, 1),
                "type_document": "CC",
                "sex": "M",
                "ethnicity": "NA",
                "headquarter": "BO",
                "PAPA": 4.7,
                "PBM": 20,
                "advance": 85.0,
                "is_enrolled": True,
                "num_semesters": 6,
                "contact_person": contact,
                "diseases": "",
                "medication": "",
                "faculty": "Ingenier\u00eda",
                "major": "ISCO",
                "admission": "REGUL",
                "study_level": "PRE",
            },
        )

    def ensure_guest_employee(self):
        user = self.ensure_user(
            "guest.employee@unal.edu.co",
            "GuestEmployee123!",
            "Guest",
            "Employee",
        )
        Employee.objects.update_or_create(
            id=900000002,
            defaults={
                "user": user,
                "birth_place": "Bogota",
                "country": "Colombia",
                "city": "Bogota",
                "phone": "3007654321",
                "address": "Local demo office",
                "birth_date": date(1990, 1, 1),
                "type_document": "CC",
                "sex": "F",
                "ethnicity": "NA",
                "headquarter": "BO",
                "dependency": "ORI",
            },
        )

    def ensure_demo_admin(self):
        if not settings.ORIUN_CREATE_DEMO_ADMIN:
            return
        self.ensure_user(
            "admin@oriun.local",
            "Admin123!",
            "Local",
            "Admin",
            is_staff=True,
            is_superuser=True,
        )

    def handle(self, *args, **options):
        csv_path = os.path.abspath(options["path"])

        if not Call.objects.exists():
            self.stdout.write("No calls found. Loading base demo CSV data...")
            call_command("populate_data", path=csv_path)
        else:
            self.stdout.write("Base demo data already exists. Skipping CSV import.")

        self.ensure_guest_student()
        self.ensure_guest_employee()
        self.ensure_demo_admin()

        self.stdout.write(self.style.SUCCESS("Local bootstrap data is ready."))
