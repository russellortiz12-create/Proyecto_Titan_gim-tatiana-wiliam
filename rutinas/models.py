from django.db import models
from usuarios.models import Instructor

class ParteCuerpo(models.Model):
    id_parte_cuerpo = models.AutoField(primary_key=True)
    nombre_parte_cuerpo = models.CharField(max_length=100, unique=True)
    descripcion_parte_cuerpo = models.CharField(max_length=300, null=True, blank=True)
    estado_parte_cuerpo = models.CharField(max_length=20, default='ACTIVO')

    class Meta:
        db_table = 'parte_cuerpo'

    def __str__(self):
        return self.nombre_parte_cuerpo

class Musculo(models.Model):
    id_musculo = models.AutoField(primary_key=True)
    nombre_musculo = models.CharField(max_length=100, unique=True)
    descripcion_musculo = models.CharField(max_length=300, null=True, blank=True)
    estado_musculo = models.CharField(max_length=20, default='ACTIVO')
    id_parte_cuerpo = models.ForeignKey(ParteCuerpo, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_parte_cuerpo')

    class Meta:
        db_table = 'musculo'

    def __str__(self):
        return self.nombre_musculo

class Maquina(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    nombre_maquina = models.CharField(max_length=100, unique=True)
    descripcion_maquina = models.CharField(max_length=300, null=True, blank=True)
    marca_maquina = models.CharField(max_length=100, null=True, blank=True)
    numero_serie = models.CharField(max_length=100, unique=True, null=True, blank=True)
    ubicacion_maquina = models.CharField(max_length=100, null=True, blank=True)
    estado_maquina = models.CharField(max_length=30, default='DISPONIBLE')

    class Meta:
        db_table = 'maquina'

    def __str__(self):
        return self.nombre_maquina

class Ejercicio(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    nombre_ejercicio = models.CharField(max_length=100)
    descripcion_ejercicio = models.CharField(max_length=500)
    repeticiones_recomendadas = models.CharField(max_length=30, null=True, blank=True)
    series_recomendadas = models.CharField(max_length=30, null=True, blank=True)
    demo_url = models.CharField(max_length=300, null=True, blank=True)
    nivel_dificultad = models.CharField(max_length=30)
    tipo_ejercicio = models.CharField(max_length=30)
    estado_ejercicio = models.CharField(max_length=20, default='ACTIVO')
    id_musculo = models.ForeignKey(Musculo, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_musculo')
    id_maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_maquina')

    class Meta:
        db_table = 'ejercicio'

    def __str__(self):
        return self.nombre_ejercicio

class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    nombre_rutina = models.CharField(max_length=100)
    descripcion_rutina = models.CharField(max_length=500, null=True, blank=True)
    objetivo_rutina = models.CharField(max_length=50)
    nivel_rutina = models.CharField(max_length=30)
    duracion_semanas = models.IntegerField(null=True, blank=True)
    estado_rutina = models.CharField(max_length=20, default='ACTIVA')
    id_instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_instructor')

    class Meta:
        db_table = 'rutina'

    def __str__(self):
        return self.nombre_rutina

class RutinaEjercicio(models.Model):
    id_rutina_ejercicio = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, db_column='id_rutina')
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, db_column='id_ejercicio')
    orden_ejercicio = models.IntegerField()
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    tiempo_descanso = models.IntegerField(null=True, blank=True)
    peso_recomendado = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observaciones = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'rutina_ejercicio'

    def __str__(self):
        return f"Detalle Rutina {self.id_rutina_ejercicio}"