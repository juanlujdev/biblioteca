from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .models import Prestamo

from .forms import PrestamoForm, MultiplePrestamoForm


# Create your views here.

class RegistarPrestamo(FormView):  # utilizamos el formview xq nos permite procesos extras que el create view
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm  # FormView o CreateView necesitamos un formulario desdedonde hay q registrar los datos
    success_url = '.'  # la direccion donde quiero que valla despues de guardar el form

    def form_valid(self, form):  # el form recibe el formulario del html
        # siempre que interactuamos con la orm, llamamos al metodo objects. con create especificamos los campos con los
        # que vamos a crear el modelo prestamo

        # ESTA ES UNA FORMA DE GUARDAR DATOS DE UN FORM, el create crea de 0, crea un id nuevo cada vez q se utiliza
        # Prestamo.objects.create(
        #     lector= form.cleaned_data['lector'],#Recojo los datos de los campos de mi html
        #     libro= form.cleaned_data['libro'],
        #     fecha_prestamo=date.today(), #internamente damos datos a este campo
        #     devuelto=False #Porque directamente estamos prestando. el campo fecha_devolucion puede estar vacio en el model
        # )

        # OTRA MANERA DE GUARDAR DATOS DE UN FORM. el punto save() es parecido al update, no crea un id nuevo
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],  # Recojo los datos de los campos de mi html
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),  # internamente damos datos a este campo
            devuelto=False
            # Porque directamente estamos prestando. el campo fecha_devolucion puede estar vacio en el model
        )
        prestamo.save()

        libro = form.cleaned_data['libro']  # Asi recojo la informacion de mi objeto libro(cual es) desde mi html
        libro.stock = libro.stock - 1  # descuento 1 libro cada vez que prestamos un libor
        libro.save()

        return super(RegistarPrestamo, self).form_valid(form)

    # Lo que vamos a hacer es cambiar la manera de hacer el registro. lo que hara sera que si una persona tiene un
    # registro de prestamo ( que a cogido prestado un libro y no lo ha devuelto) y quiere volver a coger el mismo libro
    # prestado no le deje, a traves de la orm de django


class AddPrestamo(FormView):  # utilizamos el formview xq nos permite procesos extras que el create view
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm  # FormView o CreateView necesitamos un formulario desdedonde hay q registrar los datos
    success_url = '.'  # la direccion donde quiero que valla despues de guardar el form

    def form_valid(self, form):
        #para la orm get_or_create declaramos dos variables, obj donde va a estar el objeto si se ha creado o se esta
        # recuperando y el create que nos dice si se ha cresado el registro o no con un boolean.
        # Si existe lector y existe ese mismo libro y su devueltop esta a false
        obj, created= Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],  # Recojo los datos de los campos de mi html de mi formulario
            libro=form.cleaned_data['libro'],
            devuelto=False,
            defaults={ # en caso q no encuentres el registro con ese lector, ese libro y devuelto a false, puedes crear
                # un registro con esos parametros y con el defaults le paso un campo mas que quiero que registre
                'fecha_prestamo' : date.today(),
            }
        )
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')# con HttpResponseRedirect redirigimos a la pagina si no se ha creado






# REGISTRAR VARIOS PRESTAMOS DE LIBROS EN UNA SOLA VISTA
class AddMultiplePrestamo(FormView):  # utilizamos el formview xq nos permite procesos extras que el create view
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm  # FormView o CreateView necesitamos un formulario desdedonde hay q registrar los datos
    success_url = '.'  # la direccion donde quiero que valla despues de guardar el form

    def form_valid(self, form):

        prestamos=[] #declaro un array prestamos
        for l in form.cleaned_data['libros']:#asi consigo los datos d libros del html (seleccionamos)
            prestamo=Prestamo(
                lector=form.cleaned_data['lector'],
                libro=l,
                fecha_prestamo=date.today(),
                devuelto=False
            )
            prestamos.append(prestamo)
        Prestamo.objects.bulk_create(prestamos)# creará instancias de nuestro objeto a traves de una lista, asi nos
            #evitamos que para cada uno de los registros agamos un guardado y lo haga de golpe.

        return super(AddMultiplePrestamo, self).form_valid(form)