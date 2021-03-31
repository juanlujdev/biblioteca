from django.contrib import admin

from .models import Libro#Me importo los datos de libro de su model
# Register your models here.

from .models import Categoria
admin.site.register(Libro)#para que a traves de admin que viene por defecto en django podamos registrar con los datos
#que le hemos puesto en su models los priemero datos
admin.site.register(Categoria)