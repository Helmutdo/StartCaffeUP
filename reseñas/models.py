# reseñas/models.py
from django.db import models

class Reseña(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
