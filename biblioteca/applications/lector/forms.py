from django import forms

from .models import Prestamo
from ..libro.models import Libro


class PrestamoForm(forms.ModelForm):# porque estamos trabajando directamente con el modelo prestamo

    class Meta:
        model=Prestamo
        fields=(
            'lector',
            'libro',
        )

class MultiplePrestamoForm(forms.ModelForm):

    libros= forms.ModelMultipleChoiceField(
        #queryset=Libro.objects.all() podemos hacerlo asi o hacerlo como abajo
        # #queryset cual sera el conjunto de datos que va a cargar

        #le podemos pasar el conjunto de datos a traves de una funcion
        queryset=None,
        required=True,
        widget= forms.CheckboxSelectMultiple, #Con un widget decoramos un formulario, decimos q sea con check
    )

    class Meta:
        model=Prestamo
        fields=(
            'lector',
        )

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset=Libro.objects.all() # quiero inicializar el el campo libros con todos los q tenga en su bbdd