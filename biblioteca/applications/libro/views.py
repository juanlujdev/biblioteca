# CADA VEZ QUE SE HAGA UNA VISTA HAY QUE DECIRSELO EN LA URL DE LA CARPETA GENERAL, "EN ESTE CASO BIBLIOTECA"

from django.shortcuts import render
from django.views.generic import ListView, DetailView

# models local
from .models import Libro


# Create your views here.

class ListLibros(ListView):
    # model = Autor vamnos a traer la lista de autores a traves de la funcion
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')  # self es toda la informacion que esta llegando, recoge el kword
        # que le pasamos dedse el input del html como name= kword e id = kword

        f1 = self.request.GET.get("fecha1", '')# self es toda la informacion que esta llegando, recoge los valores de
        # las fechas que le pasamos desde el input del html como name= fecha1 e id=fecha1
        f2 = self.request.GET.get("fecha2", '')

        if  f1 and f2:#si f1 y f2 tienen valores, que me haga la consulta
            return Libro.objects.lista_libros2(palabra_clave, f1, f2)  # recibe el valor de la caja de texto de la palabra clave, llamo
            # a la funcion que esta en managers buscar_autor pasandoles la palabra recibida en el input "kword" y nos devuelve
            # lo que hace esa funcio, en este caso el resultado del filtrado del nombre
        else:
             return Libro.objects.lista_libros1(palabra_clave)  #si no tienen valores hagamos la consulta 1


class ListLibrosTrg(ListView):
    # model = Autor vamnos a traer la lista de autores a traves de la funcion
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')  # self es toda la informacion que esta llegando, recoge el kword
        # que le pasamos dedse el input del html como name= kword e id = kword


        return Libro.objects.lista_libros_trg(palabra_clave)  #si no tienen valores hagamos la consulta 1

class ListLibros2(ListView):
    # model = Autor vamnos a traer la lista de autores a traves de la funcion
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria(4)# para acceder al metodo listar_libros_categoria() hay que llamar
        # al objects que es nuestro manager conectado a nuestra clase


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle.html'