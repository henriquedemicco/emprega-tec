# Generated by Django 3.0.7 on 2021-06-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_userprofile_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sobrenome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
