# Generated by Django 5.0.3 on 2024-04-15 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_date_banned_mobility'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='diseases',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='medication',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission',
            field=models.CharField(choices=[('REGUL', 'Regular'), ('PAES', 'PAES'), ('PEAMA', 'PEAMA')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.contactperson'),
        ),
    ]
