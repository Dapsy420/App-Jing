# Generated by Django 4.0.4 on 2024-04-11 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0007_eventstanding_remove_university_overall_score'),
        ('Person', '0013_alter_person_user'),
        ('Sport', '0006_sportcordinator_delete_finalsportpoints_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SportCordinator',
            new_name='SportCoordinator',
        ),
        migrations.CreateModel(
            name='SportStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField()),
                ('participated', models.BooleanField(default=False)),
                ('event_sport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Sport.eventsport')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='University.university')),
            ],
        ),
    ]
