# Generated by Django 5.0.3 on 2024-04-08 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_user', models.CharField(choices=[('E', 'Estudiante'), ('T', 'Trabajador')], max_length=2)),
                ('type_document', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('PA', 'Pasaporte')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('birth_place', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('ethnicity', models.CharField(choices=[('IN', 'Indígena'), ('AF', 'Afrocolombiana'), ('RG', 'Rom o gitana'), ('NA', 'Ninguna')], default=('NA', 'Ninguna'), max_length=2)),
                ('headquarter', models.CharField(choices=[('BO', 'Bogotá'), ('AM', 'Amazonia'), ('CA', 'Caribe'), ('MA', 'Manizales'), ('ME', 'Medellín'), ('OR', 'Orinoquia'), ('PA', 'Palmira'), ('TU', 'Tumaco'), ('LP', 'La Paz')], default=('BO', 'Bogotá'), max_length=2)),
                ('dependency', models.CharField(choices=[('ORI', 'Oficina de Relaciones Interinstitucionales'), ('DRE', 'Dirección de Relaciones Exteriores')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
