from django.contrib import admin
from .models import ParteCuerpo,  Musculo, Maquina, Ejercicio,  Rutina, RutinaEjercicio

# Register your models here.

admin.site.register(ParteCuerpo)
admin.site.register(Musculo)
admin.site.register(Maquina)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(RutinaEjercicio)
