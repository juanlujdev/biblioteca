# traigo los models porque necesito sus datos
from django.db import models

from django.db.models import Q  # nla funcion Q nos ayuda a hacer las sentencias de tipo or


class AutorManager(models.Manager):  # para hacer las consultas a la bbdd
    """managers para el modelo autor"""

    # def listar_autores(self):
    #   return self.all()  # el self nos trae lo que antes conociamos como autor.object
    # para decirle que esta clase ( AutorManager) pertenece a Autor, lo hace desde models

    def buscar_autor(self, kword):  # recibe un valor que es kword

        resultado = self.filter(
            nombre__icontains=kword  # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
            # palabra que contenga el kword que recibe
        )

        return resultado

    # Buscar informacion entre nombres o apellidos
    def buscar_autor2(self, kword):  # recibe un valor que es kword

        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
            # le decimos que el filtro (que sera filtrado por nombre o apellido)  que busque cualquier
            # palabra que contenga el kword que recibe
        )

        return resultado

    # muestra el resultado excluyendo las personas que tengan una cierta edad
    def buscar_autor3(self, kword):  # recibe un valor que es kword

        resultado = self.filter(
            nombre__icontains=kword  # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
            # palabra que contenga el kword que recibe
        ).exclude(  # sacame la informacion excluyendome los que tengar esa edad
            Q(edad=55) | Q(edad=73)
        )

        return resultado

    # Autores cuya edad sean mayoy de una edad
    def buscar_autor4(self, kword):  # recibe un valor que es kword

        resultado = self.filter(
            edad__gt=40,  # gt sirve para decirle que es mayor de 40, LA COMA ES PARA DECIRLE QUE ES Y,
            edad__lt=65  # lt sirve para decirle que es mayor de 65, LA COMA ES PARA DECIRLE QUE ES Y,

        ).order_by('apellidos', 'nombre', 'id')#los ordeno en base a los apellidos, nombre e id

        return resultado
