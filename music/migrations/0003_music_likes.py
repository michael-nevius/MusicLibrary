# Generated by Django 4.0.4 on 2022-05-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_remove_music_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='likes',
            field=models.IntegerField(default=1, verbose_name=1),
            preserve_default=False,
        ),
    ]