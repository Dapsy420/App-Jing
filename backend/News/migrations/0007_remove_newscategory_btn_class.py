# Generated by Django 4.0.4 on 2022-08-13 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_alter_news_id_alter_newscategory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newscategory',
            name='btn_class',
        ),
    ]