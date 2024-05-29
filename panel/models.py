from django.db import models

# Create your models here.

from django.conf import settings

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/usuarios', verbose_name='Imagen', null=True)
    dni = models.CharField(verbose_name='DNI', max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(verbose_name='Telefono', max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Usuario relacionado')

    def __str__(self):
        return str(self.user)  # Devuelve la representación en cadena del usuario relacionado

class Proyecto(models.Model):
    ESTADO_CHOICES = (
        ('Por Aprobar', 'Pendiente'),
        ('Proyecto Aprobado', 'Aprobado'),
        ('Proyecto Rechazado', 'Rechazado'),
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


#agregar comentario proyecto 
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
    

  
    
