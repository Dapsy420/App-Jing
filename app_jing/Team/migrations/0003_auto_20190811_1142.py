# Generated by Django 2.2.2 on 2019-08-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0002_team_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='event_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='place',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
