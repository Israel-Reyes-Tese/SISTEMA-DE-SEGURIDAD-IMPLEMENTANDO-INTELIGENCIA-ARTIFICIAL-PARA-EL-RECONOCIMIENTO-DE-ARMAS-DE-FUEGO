from django.contrib import admin
from objeto_deteccion_app.models import *
@admin.register(DetectedObject)
class Sistema_seguridad_Admin(admin.ModelAdmin):
    list_display = ('id','etiqueta','probabilidad','imagen')
    list_filter = ('etiqueta',
                   'probabilidad')