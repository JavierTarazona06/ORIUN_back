# Generated by Django 5.0.3 on 2024-04-24 16:38

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('webpage', models.CharField(max_length=255)),
                ('region', models.CharField(choices=[('NA', 'Norte América'), ('LA', 'Latinoamérica'), ('EU', 'Europa'), ('OC', 'Oceanía'), ('AS', 'Oceanía'), ('AN', 'Uniandes'), ('SG', 'Convenio Sigueme/Nacional')], max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('academic_offer', models.CharField(max_length=255)),
                ('exchange_info', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('begin_date', models.DateField()),
                ('deadline', models.DateField()),
                ('min_advance', models.FloatField()),
                ('min_papa', models.FloatField()),
                ('format', models.CharField(choices=[('P', 'Presencial'), ('V', 'Virtual'), ('M', 'Mixto')], max_length=10)),
                ('study_level', models.CharField(choices=[('PRE', 'Pregrado'), ('POS', 'Postgrado'), ('DOC', 'Doctorado')], max_length=10)),
                ('year', models.SmallIntegerField()),
                ('semester', models.CharField(choices=[('1', 'Primer'), ('2', 'Segundo')], max_length=10)),
                ('language', models.CharField(choices=[('en', 'Inglés'), ('es', 'Español'), ('fr', 'Francés'), ('pt', 'Portugués'), ('de', 'Alemán'), ('it', 'Italiano'), ('ko', 'Coreano'), ('ru', 'Ruso'), ('zh', 'Chino'), ('xx', 'Otro')], max_length=5)),
                ('description', models.TextField()),
                ('available_slots', models.SmallIntegerField()),
                ('note', models.TextField(blank=True, null=True)),
                ('highest_papa_winner', models.FloatField(default=0.0)),
                ('minimum_papa_winner', models.FloatField(default=0.0)),
                ('selected', models.IntegerField(default=0)),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.university')),
            ],
        ),
    ]
