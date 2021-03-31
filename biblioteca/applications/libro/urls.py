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
]
