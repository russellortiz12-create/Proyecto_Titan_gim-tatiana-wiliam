from django.db import models
from usuarios.models import Aprendiz, Instructor, Usuario
from rutinas.models import Rutina

class SeguimientoFisico(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    id_aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE, db_column='id_aprendiz')
    id_instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_instructor')
    fecha_seguimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=3, decimal_places=2)
    porcentaje_grasa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    masa_muscular = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'seguimiento_fisico'

    def __str__(self):
        return f"Seguimiento Aprendiz {self.id_aprendiz_id} - {self.fecha_seguimiento}"

class RutinaPorUsuario(models.Model):
    id_rutina_usuario = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, db_column='id_rutina')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_instructor')
    fecha_asignacion = models.DateField()
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    objetivo_usuario = models.CharField(max_length=300, null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    estado_rutina_usuario = models.CharField(max_length=30, default='ACTIVA')

    class Meta:
        db_table = 'rutina_por_usuario'

    def __str__(self):
        return f"Rutina Usuario ID {self.id_usuario_id}"