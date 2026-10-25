from django.contrib import admin
from .models import TipoDocumento, Ficha, Usuario,  Aprendiz,  Instructor, Funcionario

# Register your models here.

admin.site.register(TipoDocumento)
admin.site.register(Ficha)
admin.site.register(Usuario)
admin.site.register(Aprendiz)
admin.site.register(Instructor)
admin.site.register(Funcionario)

