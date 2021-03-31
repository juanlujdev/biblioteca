from django.db import models

# Create your models here.
from applications.libro.models import Libro


class Lector(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=20
    )
    edad = models.PositiveIntegerField(default=0)#ponemos por defecto que si no ponemos edad nos salga en 0

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector, #campo lector hace referencia a la tabla Lector (1 a 1)
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,#campo libro hace referencia a la tabla Libro (1 a 1)
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(#No queremos q sea obligatorio porque la fecha de devolucion se actializa cuando
        #se devuelve
        blank=True,
        null=True
    )
    devuelto = models.BooleanField()

    def __str__(self):
        return self.libro.titulo
