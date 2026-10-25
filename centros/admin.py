from django.contrib import admin
from .models import CentrosFormacion, ProgramaFormacion, Dependencias

# Register your models here.

admin.site.register(CentrosFormacion)
admin.site.register(ProgramaFormacion)
admin.site.register(Dependencias)
