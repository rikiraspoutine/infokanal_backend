# Generated by Django 4.1.10 on 2023-07-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssfeedaicontent',
            name='createdat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
