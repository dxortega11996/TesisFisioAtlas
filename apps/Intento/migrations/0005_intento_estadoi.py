# Generated by Django 3.1.2 on 2021-03-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intento', '0004_auto_20210321_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='intento',
            name='estadoI',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
