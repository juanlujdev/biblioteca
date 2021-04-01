import datetime

# traigo los models porque necesito sus datos
from django.db import models

from django.db.models import Q, Count, Avg, Sum  # nla funcion Q nos ayuda a hacer las sentencias de tipo or
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):  # para hacer las consultas a la bbdd
    """procedimientos para prestamo"""

    def libros_promedio_edades(self):
        resultado = self.filter(
            # filtramos tods los libros prestados de un determinado libro. estoy en la tabla prestamo
            libro__id='1'  # en nuestro modelo Prestamo, para acceder al atributo libro es "libro"
        ).aggregate(
            promedio_edad=Avg('lector__edad'),  # accedo a mi atributo lector de models la clase prestamo
            suma_edad=Sum('lector__edad')  # como es un aggregate y devuelve diccionarios, nos permite agregar
            # informacion al diccionario. en el anotate no. ahora devuelvo la media de edad y la suma de sus edades
        )
        return resultado

    # Contar cuantas veces se ha prestado cada libro. no funciona porque no puede contar los mismos libros prestrados,
    # porque pertenecen a un resgistro( el de prestamo diferente ) video 135. hacerlo mejor desde libros. con values
    # es como si unieramos los libros con su id, en base a libros.
    def num_libros_prestados(self):
        resultado = self.values(
            'libro'  # en base a si hay libros, cuenta.
        ).annotate(
            num_prestados=Count('libro'),
            titulo=Lower('libro__titulo')# con el atrtibuto libro, la fk de Prestamo. como recupero su objeto con ,
            # 'libro' accedo a su titulo
        )
        for r in resultado:
            print("===================")
            print(r, r['num_prestados'])

        return resultado
