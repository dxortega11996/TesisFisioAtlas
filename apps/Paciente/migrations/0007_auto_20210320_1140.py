# Generated by Django 3.1.2 on 2021-03-20 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profesional', '0001_initial'),
        ('Paciente', '0006_paciente_profesional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='profesional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profesional.profesional'),
        ),
    ]