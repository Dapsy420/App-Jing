# Generated by Django 4.0.4 on 2022-08-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0004_alter_finalsportpoints_id_alter_sport_id'),
        ('Event', '0002_alter_event_id'),
        ('Placement', '0002_sportplacement_participated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventplacement',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placements', to='Event.event'),
        ),
        migrations.AlterField(
            model_name='sportplacement',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placements', to='Sport.sport'),
        ),
    ]
