# Generated by Django 3.1.2 on 2021-03-08 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='escenario',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='nivel',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='notificacion',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='puntaje_definido',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='tiempo_definido',
        ),
    ]
