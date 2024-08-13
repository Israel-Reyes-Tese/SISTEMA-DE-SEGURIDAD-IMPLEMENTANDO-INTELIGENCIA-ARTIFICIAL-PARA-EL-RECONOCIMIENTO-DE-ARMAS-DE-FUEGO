from django.db import models

# Create your models here.
from django.db import models

class DetectedObject(models.Model):

    etiqueta = models.CharField(max_length=255)
    probabilidad = models.FloatField(default=0.0)

    x =  models.FloatField(default=0.0)
    y =  models.FloatField(default=0.0)
    w = models.FloatField(default=0.0)
    h = models.FloatField(default=0.0)

    imagen = models.ImageField(upload_to='images/armas_fuego')
    creada = models.DateTimeField(auto_now_add=True)

    clase = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.etiqueta} - {self.probabilidad}%'
