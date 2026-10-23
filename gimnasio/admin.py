from django.contrib import admin
from .models import (
    TipoDocumento, CentrosFormacion, ProgramaFormacion, 
    Ficha, Usuario, Aprendiz, Instructor, Dependencias, Funcionario
)

admin.site.register(TipoDocumento)
admin.site.register(CentrosFormacion)
admin.site.register(ProgramaFormacion)
admin.site.register(Ficha)
admin.site.register(Usuario)
admin.site.register(Aprendiz)
admin.site.register(Instructor)
admin.site.register(Funcionario)


