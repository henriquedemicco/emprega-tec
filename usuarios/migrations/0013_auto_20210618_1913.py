# Generated by Django 3.0.7 on 2021-06-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20210618_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cv',
            field=models.FileField(blank=True, upload_to='media', verbose_name='Currículo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Foto'),
        ),
    ]
