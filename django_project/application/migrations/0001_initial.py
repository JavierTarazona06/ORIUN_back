# Generated by Django 5.0.3 on 2024-04-08 14:44

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
                ('doc_id_student', models.CharField(max_length=255)),
                ('approved', models.BooleanField(null=True)),
                ('is_extension', models.BooleanField()),
                ('comment_approved', models.TextField(null=True)),
                ('approve_documents', models.BooleanField()),
                ('comment_docs', models.TextField(null=True)),
                ('destination_faculty', models.CharField(max_length=50)),
                ('destination_program', models.CharField(max_length=50)),
                ('dest_contact_email', models.CharField(max_length=50)),
                ('dest_contact_name', models.CharField(max_length=50)),
                ('dest_contact_position', models.CharField(max_length=50)),
                ('dest_contact_cellphone', models.CharField(max_length=50)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('info_courses', models.JSONField()),
                ('diseases', models.TextField()),
                ('medication', models.TextField()),
                ('other_documents', models.JSONField()),
                ('grades_certificate', models.CharField(max_length=255)),
                ('training_session', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), size=None)),
                ('call_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.call')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
