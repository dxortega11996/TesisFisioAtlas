# Generated by Django 3.1.2 on 2021-04-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0006_control_ordern'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='control',
            name='ordern',
        ),
        migrations.AddField(
            model_name='control',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]