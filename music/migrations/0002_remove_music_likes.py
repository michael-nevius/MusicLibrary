# Generated by Django 4.0.4 on 2022-05-06 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='likes',
        ),
    ]
