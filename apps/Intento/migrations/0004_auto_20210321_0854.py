# Generated by Django 3.1.2 on 2021-03-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intento', '0003_auto_20210307_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='intento',
            name='dificultad',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='intento',
            name='tipoJuego',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
