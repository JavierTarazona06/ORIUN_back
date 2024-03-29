# Generated by Django 5.0.3 on 2024-03-29 22:27

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('webpage', models.TextField()),
                ('region', models.CharField(choices=[('NA', 'Norte América')], max_length=2)),
                ('country', models.TextField()),
                ('city', models.TextField()),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('en', 'Inglés')], max_length=2), size=None)),
                ('academic_offer', models.TextField()),
                ('exchange_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('begin_date', models.DateField()),
                ('deadline', models.DateField()),
                ('min_advance', models.SmallIntegerField()),
                ('min_papa', models.SmallIntegerField()),
                ('format', models.CharField(choices=[('P', 'Presencial')], max_length=1)),
                ('study_level', models.CharField(choices=[('P', 'Pregrado')], max_length=1)),
                ('year', models.SmallIntegerField()),
                ('semester', models.CharField(choices=[(1, 'First'), (2, 'Second')])),
                ('description', models.TextField()),
                ('available_slots', models.SmallIntegerField()),
                ('note', models.TextField(blank=True, null=True)),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.university')),
            ],
        ),
    ]
