# Generated by Django 3.1.11 on 2022-07-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
