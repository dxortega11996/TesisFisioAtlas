# Generated by Django 3.1.2 on 2021-02-04 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Juego', '0001_initial'),
        ('Rutina', '0003_auto_20210204_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='RutinaJuego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel1', models.BooleanField(blank=True, null=True)),
                ('nivel2', models.BooleanField(blank=True, null=True)),
                ('juego', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Juego.juego')),
                ('rutina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Rutina.rutina')),
            ],
        ),
    ]
