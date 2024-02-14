from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_lenght=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categoria"
        def __str__(self):
            return self.nombre
    
    
class Post(models.Model):
    titulo=models.CharField(max_lenght=70)
    contenido=models.CharField(max_lenght=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="titulo"
        verbose_name_plural="titulos"
        def __str__(self):
            return self.titulo
    
    