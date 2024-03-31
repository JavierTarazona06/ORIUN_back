# Generated by Django 5.0.3 on 2024-03-31 02:45

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
                ('type_document', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjera'), ('PA', 'Pasaporte')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=1)),
                ('birth_place', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('ethnicity', models.CharField(choices=[('I', 'Indígena'), ('A', 'Afrocolombiana'), ('RG', 'Rom o gitana'), ('N', 'Ninguna')], default='N', max_length=2)),
                ('headquarter', models.CharField(choices=[('A', 'Amazonia'), ('C', 'Caribe'), ('B', 'Bogotá'), ('MA', 'Manizales'), ('ME', 'Medellin'), ('O', 'Orinoquía'), ('P', 'Palmira'), ('T', 'Tumaco'), ('LP', 'La Paz')], default='B', max_length=2)),
                ('dependency', models.CharField(choices=[('ORI', 'Oficina de Relaciones Interinstitucionales'), ('DRE', 'Dirección de Relaciones Internacionales')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
