# Generated by Django 4.0.4 on 2024-04-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0006_alter_university_id_alter_universityevent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='university',
            name='overall_score',
        ),
    ]
