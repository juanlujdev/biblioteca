from django.db import models
from django.db.models.signals import post_save  # post_save = lo que pasa despuesde guardar

#APPs terceros
from PIL import Image


# from local apps
from applications.autor.models import Autor
# Create your models here.
from .managers import LibroManager, CategoriaManager


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=30
    )
    objects = CategoriaManager()  # conectamos nuestro manageer a nuestro model importandonos nuestra clase y igualando a objects

    # como es una clase se pone ()

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre  # para mostrar el id en admin, como es un numero hay q convertirlo
        # a string


class Libro(models.Model):
    categoria = models.ForeignKey(  # el campo categoria Hace referencia a la tabla Categoria
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro'
        # es la manera que tenemos de acceder de categorias a libro(porque queremso listar
        # las categorias  a las que pertenece un autor. mirar relacion de la bbdd )
    )
    autores = models.ManyToManyField(
        Autor)  # la relacion segun el esquema es q un libro puede estar escrito por varios autores
    # y un autor puede escribir varios libros, relacion muchos a muchos, como esto puede ser una lista autores seria un array
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')  # upload_to es dondes se almacenan las imagenes

    visitas = models.PositiveIntegerField()
    # Agrego un campo que sera el stock para el tema de los libros que hemos prestados
    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager()  # conectamos nuestro manageer a nuestro model importandonos nuestra clase y igualando a objects

    # como es una clase se pone ()

    def __str__(self):
        return str(self.id) + "-" + self.titulo  # como devolvemos en el admin el id y es un int se tiene q convertir
        # a string


def optimize_image(sender, instance, **kwargs):  # sender=hacia donde se va a ejecutar la funcion, instance= instancia
    # a la que estamos trabajando en ese momento, lo q traemos o hemos guardado
    print("=============")
    if instance.portada:
        portada=Image.open(instance.portada.path)# asi sacamos la ruta donde tenemos guardado esa imagen
        portada.save(instance.portada.path, quality=20, optimize=True)#decicmos que nos baje la calidad de la imagen
        # un 20% y la optimizamos


post_save.connect(optimize_image,
                  sender=Libro)  # conectamos la funcion q queremos trabajar y en q modelo quiero trabajar
