# Generated by Django 4.0.4 on 2024-03-12 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0003_event_closed'),
        ('Person', '0010_remove_person_has_avatar_remove_person_is_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='event',
        ),
        migrations.CreateModel(
            name='PER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.person')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.role')),
            ],
        ),
    ]