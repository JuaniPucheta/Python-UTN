from django.db import models

# Create your models here.

class Socio(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):                              #? Para que muestre el nombre y apellido en vez de Socio object
        return self.nombre + ' ' + self.apellido