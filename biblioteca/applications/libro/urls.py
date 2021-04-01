#Creo un fichero urls.py para crear nuestra vista
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [#pongo el nombre . creo una nueva vista
    path(
        'libros/',
        views.ListLibros.as_view(),
         name="libros"
    ),
path(
        'libros-2/',
        views.ListLibros2.as_view(),
         name="libros2"
    ),
path(
        'libro-detalle/<pk>',# vamos a sacar el detalle de un libro, a traves de su id, por eso su pk
        views.LibroDetailView.as_view(),
         name="libros-detalle"
    ),
path(
        'libros-trg',# vamos a sacar el detalle de un libro, a traves de su id, por eso su pk
        views.ListLibrosTrg.as_view(),
         name="libros-detalle"
    ),
]
