# Generated by Django 3.2.12 on 2023-05-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0032_day001_day002_day003_day004_day005_day006_day007_day008_day009_day010_day011_day012_day013_day014_da'),
    ]

    operations = [
        migrations.CreateModel(
            name='KDHT001',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('links', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KDHT002',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('links', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KDHT003',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('links', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KDHT004',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('links', models.CharField(max_length=50)),
            ],
        ),
    ]
