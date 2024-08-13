# Generated by Django 3.2.23 on 2024-01-12 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objeto_deteccion_app', '0003_alter_detectedobject_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectedobject',
            name='h',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='detectedobject',
            name='w',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='detectedobject',
            name='x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='detectedobject',
            name='y',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='detectedobject',
            name='imagen',
            field=models.ImageField(upload_to='images/armas_fuego'),
        ),
        migrations.AlterField(
            model_name='detectedobject',
            name='probabilidad',
            field=models.FloatField(default=0.0),
        ),
    ]
