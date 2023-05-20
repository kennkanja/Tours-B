# Generated by Django 3.2.12 on 2023-05-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_remove_tour_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('links', models.CharField(max_length=50)),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
