# Generated by Django 3.1.2 on 2021-04-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rutina', '0003_auto_20210204_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='estado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
