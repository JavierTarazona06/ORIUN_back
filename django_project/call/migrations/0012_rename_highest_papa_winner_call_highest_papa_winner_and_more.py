# Generated by Django 5.0.3 on 2024-04-05 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0011_remove_call_highest_papa_winner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='highest_PAPA_winner',
            new_name='highest_papa_winner',
        ),
        migrations.RenameField(
            model_name='call',
            old_name='minium_PAPA_winner',
            new_name='minimum_papa_winner',
        ),
    ]
