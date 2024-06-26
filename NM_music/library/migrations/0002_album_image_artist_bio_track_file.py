# Generated by Django 5.0.4 on 2024-04-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, upload_to='album_covers/'),
        ),
        migrations.AddField(
            model_name='artist',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(blank=True, upload_to='tracks/'),
        ),
    ]
