from django.db import models
from centros.models import ProgramaFormacion, Dependencias

class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=30)
    descripcion_tipo_documento = models.CharField(max_length=40)

    class Meta:
        db_table = 'tipodocumento'

    def __str__(self):
        return self.nombre_tipo_documento

class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    numero_ficha = models.CharField(max_length=20, unique=True)
    jornada = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=20, default='PRESENCIAL')
    etapa_formacion = models.CharField(max_length=20)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado_ficha = models.CharField(max_length=20, default='ACTIVA')
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
        return f"Ficha {self.numero_ficha}"

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    ROLES_CHOICES = [
        ('APRENDIZ', 'Aprendiz'),
        ('FUNCIONARIO', 'Funcionario'),
        ('ENTRENADOR', 'Entrenador'),
        ('ADMINISTRADOR', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES_CHOICES, default='APRENDIZ')
    id_tipo_documento = models.ForeignKey(
        TipoDocumento, 
        on_delete=models.CASCADE, 
        db_column='id_tipo_documento'
    )
    numero_documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    foto_perfil_url = models.CharField(max_length=300, null=True, blank=True)
    estado_usuario = models.CharField(max_length=20, default='ACTIVO')
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.rol})"

class Aprendiz(models.Model):
    id_aprendiz = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_ficha = models.ForeignKey(Ficha, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_ficha')
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    estatura = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    tipo_sangre = models.CharField(max_length=5, null=True, blank=True)
    contacto_emergencia = models.CharField(max_length=100, null=True, blank=True)
    telefono_emergencia = models.CharField(max_length=20, null=True, blank=True)
    restricciones_medicas = models.CharField(max_length=300, null=True, blank=True)
    estado_aprendiz = models.CharField(max_length=20, default='ACTIVO')

    class Meta:
        db_table = 'aprendiz'

    def __str__(self):
        return f"Aprendiz ID: {self.id_aprendiz}"

class Instructor(models.Model):
    id_instructor = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, db_column='id_usuario')
    profesion = models.CharField(max_length=100, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    estado_instructor = models.CharField(max_length=20, default='ACTIVO')

    class Meta:
        db_table = 'instructor'

    def __str__(self):
        return f"Instructor: {self.especialidad or 'General'}"

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, db_column='id_usuario')
    id_dependencia = models.ForeignKey(Dependencias, on_delete=models.CASCADE, db_column='id_dependencia')
    vinculacion = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    fecha_terminacion = models.DateField(null=True, blank=True)
    estado_funcionario = models.CharField(max_length=20, default='ACTIVO')
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    estatura = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tipo_sangre = models.CharField(max_length=5)
    contacto_emergencia = models.CharField(max_length=100, blank=True)
    telefono_emergencia = models.CharField(max_length=20, blank=True)
    restricciones_medicas = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'funcionario'

    def __str__(self):
        return f"{self.cargo}"