from django.db import models
from datetime import date
from django.conf import settings

#categorias modalidad
class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo
    
#extencion para usuarios
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/usuarios', verbose_name='Imagen', null=True)
    dni = models.CharField(verbose_name='DNI', max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(verbose_name='Telefono', max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Usuario relacionado')

    def __str__(self):
        return str(self.user)  

#agregacion de formularios de perfil
class Proyecto(models.Model):
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    )
    titulo = models.CharField(max_length=150, verbose_name='Titulo')
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(verbose_name='Descripcion', blank=True)
    documentacion = models.FileField(upload_to='documento/proyecto', verbose_name='Documentacion', null=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona relacionada')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    destacado = models.BooleanField(default=True) 
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Por Aprobar')

    def __str__(self):
        return self.titulo


#agregar comentario formulario proyecto 
class Commentario(models.Model):
    comentari = models.TextField(max_length=1000, help_text='',verbose_name='Ingrese Comentario Retroalimentativo')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    Fecha_post = models.DateTimeField(auto_now_add=True)
    proyecto_relacionado = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-Fecha_post']

    def __str__(self):
        len_title = 15
        if len(self.comentari) > len_title:
            return self.comentari[:len_title] + '...'
        return self.comentari
    
    
    
    
    
########  espacio de poryectos de interaccion social docentes  ##########

#tipo de proyecto de interaccion social docentes
class T_Tipo_Proyecto(models.Model):
    Id_tipo=models.AutoField(primary_key=True)
    S_Tipo= models.CharField(max_length=100, verbose_name='Tipo')
    
    def __str__(self):
        return self.S_Tipo

#tipo fase de interaccion social docentes
class T_Fase_proyecto(models.Model):
    Id_fase= models.AutoField(primary_key=True)
    S_Fase=models.CharField(max_length=100,verbose_name='Fase')
    
    def __str__(self):
        return self.S_Fase 
    
#tipo gestion de interaccion social docentes
class T_Gestion(models.Model):
    Id_Ges=models.AutoField(primary_key=True)
    S_Gestion= models.CharField(max_length=100,verbose_name='Nom_Gestion')
    
    def __str__(self):
        return self.S_Gestion
    
#tipo semestre de interaccion social docentes
class T_Semestre(models.Model):
    Id_Semestre= models.AutoField(primary_key=True)
    S_Semestre=models.CharField(max_length=100,verbose_name='Semestre')
    
    def __str__(self):
        return self.S_Semestre 

#tipo materia de interaccion social docentes  
class T_Materia(models.Model):
    Id_Materia= models.AutoField(primary_key=True)
    S_Materia=models.CharField(max_length=100,verbose_name='Materia')
    T_Semestre=models.ForeignKey(T_Semestre, on_delete=models.CASCADE, verbose_name="Semestre")
    def __str__(self):
        return self.S_Materia
    
#tipo agregacion de poryecto de interaccion social docentes
class T_Proyectos(models.Model):
    Id_Proyect = models.AutoField(primary_key=True)
    S_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona relacionada')
    S_Titulo = models.CharField(max_length=150, verbose_name='Titulo')
    Fecha_Inicio = models.DateField(auto_now=False, auto_now_add=False)
    Fecha_Finalizacion = models.DateField(auto_now=False, auto_now_add=False)
    S_Descripcion = models.TextField(verbose_name='Descripcion', blank=True)
    S_Documentacion = models.FileField(upload_to='Documento/', verbose_name='Documentacion', null=True)
    S_Imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    T_Fase_proyecto = models.ForeignKey(T_Fase_proyecto, on_delete=models.CASCADE, verbose_name='Fase del Proyecto')
    T_Gestion = models.ForeignKey(T_Gestion, on_delete=models.CASCADE, verbose_name='Gestion')
    T_Tipo_Proyecto = models.ForeignKey(T_Tipo_Proyecto, on_delete=models.CASCADE, verbose_name='Tipo de Proyecto')
    T_Materia = models.ForeignKey(T_Materia, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Materia')
     
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.Fecha_Finalizacion < self.Fecha_Inicio:
            raise ValidationError('La fecha de finalización debe ser posterior a la fecha de inicio.')
        
    def __str__(self):
        return self.S_Titulo
    
class GlobalSettings(models.Model):
    habilitar_proyectos = models.BooleanField(default=True, verbose_name='Habilitar Proyectos')
    fecha_inicio_habilitacion = models.DateField(null=True, blank=True, verbose_name='Fecha de Inicio de Habilitación')
    fecha_fin_habilitacion = models.DateField(null=True, blank=True, verbose_name='Fecha Fin de Habilitación')

    def __str__(self):
        return "Configuración Global"

    def tiempo_restante(self):
        hoy = date.today()
        if self.fecha_fin_habilitacion and hoy <= self.fecha_fin_habilitacion:
            return (self.fecha_fin_habilitacion - hoy).days
        return None
  
    

  
    
