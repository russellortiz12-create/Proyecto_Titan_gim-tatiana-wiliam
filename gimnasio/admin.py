from django.contrib import admin
from .models import TipoDocumento, ProgramaFormacion, Ficha, CentrosFormacion

admin.site.register(TipoDocumento)
admin.site.register(CentrosFormacion)
admin.site.register(ProgramaFormacion)
admin.site.register(Ficha)