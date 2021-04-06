# Creo un fichero urls.py para crear nuestra vista
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [  # pongo el nombre . creo una nueva vista
    path(
        'prestamo/add/',
        views.AddPrestamo.as_view(),
        name="prestamo-add"
    ),
    path(
        'prestamo/multiple-add/',
        views.AddMultiplePrestamo.as_view(),
        name="prestamo_add_multiple"
    ),
]
