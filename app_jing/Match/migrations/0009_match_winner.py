# Generated by Django 2.2.2 on 2019-08-12 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0003_auto_20190811_1142'),
        ('Match', '0008_auto_20190807_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Team.Team'),
        ),
    ]
