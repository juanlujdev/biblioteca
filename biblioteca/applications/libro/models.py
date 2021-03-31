from django.db import models

# from local apps
from applications.autor.models import Autor
# Create your models here.
from .managers import LibroManager


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(  # el campo categoria Hace referencia a la tabla Categoria
        Categoria,
        on_delete=models.CASCADE,
    )
    autores = models.ManyToManyField(
        Autor)  # la relacion segun el esquema es q un libro puede estar escrito por varios autores
    # y un autor puede escribir varios libros, relacion muchos a muchos
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')  # upload_to es dondes se almacenan las imagenes

    visitas = models.PositiveIntegerField()

    objects = LibroManager()  # conectamos nuestro manageer a nuestro model importandonos nuestra clase y igualando a objects

    # como es una clase se pone ()

    def __str__(self):
        return self.titulo
