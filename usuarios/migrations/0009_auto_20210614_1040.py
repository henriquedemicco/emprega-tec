# Generated by Django 3.0.7 on 2021-06-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20210614_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cv',
            field=models.FileField(blank=True, upload_to='cvs', verbose_name='Currículo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos', verbose_name='Foto'),
        ),
    ]