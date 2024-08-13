# Generated by Django 3.2.23 on 2024-01-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetectedObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.CharField(max_length=255)),
                ('probabilidad', models.FloatField()),
                ('imagen', models.ImageField(upload_to='detected_images/')),
                ('creada', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]