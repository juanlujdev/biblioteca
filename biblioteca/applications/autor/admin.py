from django.contrib import admin

from .models import Autor#Me importo los datos de autor de su model
# Register your models here.

admin.site.register(Autor)#para que a traves de admin que viene por defecto en django podamos registrar con los datos
#que le hemos puesto en su models los priemero datos