# Generated by Django 3.0.7 on 2021-06-16 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_candidatura_experiencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatura',
            name='curso',
        ),
    ]
