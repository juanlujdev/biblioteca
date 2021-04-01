from django.db import models

# Create your models here.
from applications.lector.managers import PrestamoManager
from applications.libro.models import Libro


# from managers


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
    edad = models.PositiveIntegerField(default=0)  # ponemos por defecto que si no ponemos edad nos salga en 0

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,  # campo lector hace referencia a la tabla Lector (1 a 1)
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,  # campo libro hace referencia a la tabla Libro (1 a 1)
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
        # porque necesitamos invertir la FK para el ejercicio , contar cuantas veces prestamos
        # un libro. como lo facil es coger un libro y ver las veces que se ha prestado, pero en la tabla libro no tiene relacion
        # o fk con prestado, pero si al reves. por lo tanto para invertir esa FK se utiliza realete_name
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        # No queremos q sea obligatorio porque la fecha de devolucion se actializa cuando
        # se devuelve
        blank=True,
        null=True
    )
    devuelto = models.BooleanField()

    objects = PrestamoManager()  # vinculacion de models con el manager

    def __str__(self):
        return self.libro.titulo
