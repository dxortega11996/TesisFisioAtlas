# Generated by Django 3.1.2 on 2020-11-18 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('temperatura', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('talla', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('imc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('frec_respiratoria', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('frec_cardiaca', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('presion_arterial', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
