# Generated by Django 4.0.4 on 2022-08-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Match', '0017_matchteam_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchteam',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
    ]