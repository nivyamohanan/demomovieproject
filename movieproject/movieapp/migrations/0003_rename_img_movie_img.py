# Generated by Django 3.2.15 on 2022-08-13 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='IMG',
            new_name='img',
        ),
    ]
