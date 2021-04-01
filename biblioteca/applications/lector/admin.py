from django.contrib import admin

# Register your models here.
from .models import Lector
from .models import Prestamo

admin.site.register(Lector)#para que a traves de admin que viene por defecto en django podamos registrar con los datos
#que le hemos puesto en su models los priemero datos
admin.site.register(Prestamo)