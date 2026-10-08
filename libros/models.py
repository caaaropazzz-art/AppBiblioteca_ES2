from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20, unique=True)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo