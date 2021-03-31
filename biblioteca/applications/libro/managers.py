import datetime

# traigo los models porque necesito sus datos
from django.db import models

from django.db.models import Q  # nla funcion Q nos ayuda a hacer las sentencias de tipo or


class LibroManager(models.Manager):  # para hacer las consultas a la bbdd
    """managers para el modelo autor"""

    # def listar_autores(self):
    #   return self.all()  # el self nos trae lo que antes conociamos como autor.object
    # para decirle que esta clase ( AutorManager) pertenece a Autor, lo hace desde models

    def lista_libros1(self, kword):  # recibe un valor que es kword

        resultado = self.filter(
            titulo__icontains=kword,  # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
            # palabra que contenga el kword que recibe. LA COMA ES UN Y
            fecha__range=('2000-01-01','2021-03-07')# y que nos traiga los libros con este rango de fecha
        )

        return resultado

    def lista_libros2(self, kword, fecha1, fecha2):  # recibe el valor que es kword, y las fechas

        date1=datetime.datetime.strptime(fecha1,'%Y-%m-%d').date()#manera de convertir las fechas al formato deseado
        date2=datetime.datetime.strptime(fecha2,'%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=kword,  # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
            # palabra que contenga el kword que recibe. LA COMA ES UN Y
            fecha__range=(date1,date2)# y que nos traiga los libros con este rango de fecha
        )

        return resultado
