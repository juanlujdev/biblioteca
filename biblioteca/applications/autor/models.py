from django.db import models

# managers
from .managers import AutorManager  # importo el manager que nos hace la consulta


# a la bbdd

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=30
    )
    edad = models.PositiveIntegerField()  # por defecto te da validadion de numero positivo

    # La clase Persona tiene que devolver algo
    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellidos

    class Meta:
        abstract = True  # Autor y lector heredan de esta clase de Persona, asi no se creara la gabla perosna pero si
        # que Autor y lector tendran sus atributos


class Autor(Persona):
    seudonimo = models.CharField(
        'seudonimo',
        max_length=50,
        blank=True
    )

    # para conectar la clase AutorManager de managers con la clase Autor, se hace desde
    # su objects de la clase. luego vamos a las vistas para que en return de esa vista lo
    # devuelva los datos desde el manager
    objects = AutorManager()
