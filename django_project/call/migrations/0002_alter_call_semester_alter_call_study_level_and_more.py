# Generated by Django 5.0.3 on 2024-03-31 03:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='semester',
            field=models.CharField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth'), (9, 'Ninth'), (10, 'Tenth'), (11, 'Eleventh'), (12, 'Twelfth')], max_length=10),
        ),
        migrations.AlterField(
            model_name='call',
            name='study_level',
            field=models.CharField(choices=[('PRE', 'Pregrado'), ('POS', 'Posgrado'), ('DOC', 'Doctorado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='university',
            name='language',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('en', 'Inglés'), ('es', 'Español'), ('fr', 'Francés'), ('de', 'Alemán'), ('it', 'Italiano'), ('pt', 'Portugués'), ('zh', 'Chino'), ('ja', 'Japonés'), ('ko', 'Coreano'), ('ar', 'Árabe'), ('ru', 'Ruso'), ('hi', 'Hindi')], max_length=2), size=None),
        ),
        migrations.AlterField(
            model_name='university',
            name='region',
            field=models.CharField(choices=[('NA', 'Norte América'), ('CA', 'Centro América'), ('SA', 'Sur América'), ('EU', 'Europa'), ('AS', 'Asia'), ('AF', 'África'), ('OC', 'Oceanía'), ('AN', 'Antártida')], max_length=2),
        ),
    ]
