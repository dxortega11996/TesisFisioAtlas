# Generated by Django 3.1.2 on 2021-03-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intento', '0002_auto_20210307_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intento',
            name='tiempo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
