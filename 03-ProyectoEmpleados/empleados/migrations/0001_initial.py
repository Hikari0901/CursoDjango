# Generated by Django 5.0.6 on 2024-06-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('job', models.CharField(max_length=50, verbose_name='Trabajo')),
                ('imagen', models.ImageField(upload_to=None, verbose_name='Carga una imagen personal')),
            ],
        ),
    ]
