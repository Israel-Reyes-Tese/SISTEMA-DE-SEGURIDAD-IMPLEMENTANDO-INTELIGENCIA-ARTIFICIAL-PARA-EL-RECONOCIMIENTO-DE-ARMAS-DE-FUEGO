# Generated by Django 3.2.23 on 2024-01-12 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objeto_deteccion_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectedobject',
            name='imagen',
            field=models.ImageField(upload_to='images/armas_fuego'),
        ),
    ]