from django.db import models

class CentrosFormacion(models.Model):
    id_centro = models.AutoField(primary_key=True)
    nombre_centro = models.CharField(max_length=150)
    descripcion_centro = models.TextField(null=True, blank=True)
    direccion_centro = models.CharField(max_length=255)
    telefono_centro = models.CharField(max_length=50, null=True, blank=True)
    email_centro = models.CharField(max_length=100, null=True, blank=True)
    sitio_web = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'centros_formacion'

    def __str__(self):
        return self.nombre_centro

class ProgramaFormacion(models.Model):
    id_programa_formacion = models.AutoField(primary_key=True)
    codigo_programa = models.CharField(max_length=20, unique=True)
    nombre_programa = models.CharField(max_length=150)
    nivel_programa = models.CharField(max_length=30)
    id_centro_formacion = models.ForeignKey(
        CentrosFormacion, 
        on_delete=models.CASCADE, 
        db_column='id_centro_formacion'
    )
    estado_programa = models.CharField(max_length=20, default='ACTIVO')

    class Meta:
        db_table = 'programa_formacion'

    def __str__(self):
        return f"{self.codigo_programa} - {self.nombre_programa}"

class Dependencias(models.Model):
    id_dependencia = models.AutoField(primary_key=True)
    id_centro_formacion = models.ForeignKey(
        CentrosFormacion, 
        on_delete=models.CASCADE, 
        db_column='id_centro_formacion'
    )
    nombre_dependencia = models.CharField(max_length=120)
    descripcion_dependencia = models.TextField(null=True, blank=True)
    ubicacion_dependencia = models.CharField(max_length=200, null=True, blank=True)
    telefono_dependencia = models.CharField(max_length=30, null=True, blank=True)
    email_dependencia = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'dependencias'

    def __str__(self):
        return self.nombre_dependencia