# Generated by Django 3.1.2 on 2020-11-18 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto/')),
                ('autoidentificacion', models.CharField(blank=True, max_length=30, null=True)),
                ('formacion', models.CharField(blank=True, max_length=100, null=True)),
                ('codigoMSP', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]