# Generated by Django 5.0.3 on 2024-03-29 22:27

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('call', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id_student', models.TextField()),
                ('approved', models.BooleanField()),
                ('is_extension', models.BooleanField()),
                ('approve_documents', models.BooleanField()),
                ('destination_faculty', models.TextField()),
                ('destination_program', models.TextField()),
                ('dest_contact_email', models.TextField()),
                ('dest_contact_name', models.TextField()),
                ('dest_contact_position', models.TextField()),
                ('dest_contact_cellphone', models.TextField()),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('info_courses', models.JSONField()),
                ('diseases', models.TextField()),
                ('medication', models.TextField()),
                ('other_documents', models.JSONField()),
                ('grades_certificate', models.TextField()),
                ('training_session', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), size=None)),
                ('call_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.call')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
