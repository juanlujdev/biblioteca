from django.db import models

# Create your models here.
from applications.lector.managers import PrestamoManager
from applications.libro.models import Libro
from applications.autor.models import Persona

# from managers


class Lector(Persona): # heredo los atributos de Persona q esta en la clase autor
    class Meta:
        verbose_name='Lector' #verbose es como quiero que aparezca en el admin
        verbose_name_plural='Lectores'#verbose_ pñura es como quiero que aparezca en el admin
        


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
