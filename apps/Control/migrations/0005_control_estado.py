# Generated by Django 3.1.2 on 2021-03-31 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0004_control_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='control',
            name='estado',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
