# Generated by Django 3.1.2 on 2021-03-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0007_auto_20210320_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='patologia',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]