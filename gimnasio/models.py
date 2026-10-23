from django.db import models

class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=30)
    descripcion_tipo_documento = models.CharField(max_length=40)

    class Meta:
        db_table = 'tipodocumento'

    def __str__(self):
        return self.nombre_tipo_documento


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
    estado_programa = models.CharField(max_length=20, default='ACTIVO')
    
    # Nueva llave foránea hacia el centro de formación según tu SQL actualizado:
    id_centro_formacion = models.ForeignKey(
        CentrosFormacion, 
        on_delete=models.CASCADE, 
        db_column='id_centro_formacion'
    )

    class Meta:
        db_table = 'programa_formacion'

    def __str__(self):
        return f"{self.codigo_programa} - {self.nombre_programa}"

class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    numero_ficha = models.CharField(max_length=20, unique=True)
    jornada = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=20, default='PRESENCIAL')
    etapa_formacion = models.CharField(max_length=20)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado_ficha = models.CharField(max_length=20, default='ACTIVA')
    
    # Relación de Llave Foránea con Programa de Formación
    id_programa_formacion = models.ForeignKey(
        ProgramaFormacion, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='id_programa_formacion'
    )

    class Meta:
        db_table = 'ficha'

    def __str__(self):
        return self.numero_ficha