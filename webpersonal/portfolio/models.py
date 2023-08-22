from django.db import models

# Create your models here.
class Project(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to="projects")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de mofificacion")
    link=models.URLField(null=True,blank=True)

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=["-created"]
    def __str__(self):
        return self.titulo