# Generated by Django 3.1.6 on 2021-02-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_server', '0002_auto_20210221_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiletokensession',
            name='token',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
