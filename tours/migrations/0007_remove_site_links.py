# Generated by Django 3.2.12 on 2023-05-22 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='links',
        ),
    ]
