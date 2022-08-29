from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "titulo")
    description = models.TextField(verbose_name="descripción")
    image = models.ImageField(verbose_name="imagen", upload_to = "media")
    link = models.URLField(verbose_name="Direccion web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha de modificación")

    def __str__(self):
        return self.title

class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "proyectos"
    ordering = ["-created"]

    