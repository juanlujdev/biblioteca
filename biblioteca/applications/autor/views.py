#CADA VEZ QUE SE HAGA UNA VISTA HAY QUE DECIRSELO EN LA URL DE LA CARPETA GENERAL, "EN ESTE CASO BIBLIOTECA"
from django.shortcuts import render
from django.views.generic import ListView

# models local
from .models import Autor


# Create your views here.

class ListAutores(ListView):
    # model = Autor vamnos a traer la lista de autores a traves de la funcion
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')# self es toda la informacion que esta llegando, recoge el kword
        # que le pasamos dedse el input del html como name= kword e id = kword



        # return Autor.objects.all()#traer todo los datos de Autor
        #return Autor.objects.listar_autores()  # se devuelve la consulta desde models
        return Autor.objects.buscar_autor4(palabra_clave)#recibe el valor de la caja de texto de la palabra clave, llamo
    # a la funcion que esta en managers buscar_autor pasandoles la palabra recibida en el input "kword" y nos devuelve
    # lo que hace esa funcio, en este caso el resultado del filtrado del nombre