# Generated by Django 4.0.4 on 2022-08-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Placement', '0003_alter_eventplacement_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventplacement',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]