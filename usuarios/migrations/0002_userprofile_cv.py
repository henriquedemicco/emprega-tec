# Generated by Django 3.0.7 on 2021-06-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cv',
            field=models.FileField(blank=True, upload_to='', verbose_name='Currículo'),
        ),
    ]
