# Generated by Django 2.2.2 on 2019-08-06 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Event.Event'),
            preserve_default=False,
        ),
    ]
