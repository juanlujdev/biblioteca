import datetime

# traigo los models porque necesito sus datos

from django.db import models

from django.db.models import Q, Count  # nla funcion Q nos ayuda a hacer las sentencias de tipo or

from django.contrib.postgres.search import TrigramSimilarity  # para el buscador que henmos instalado en psql


class LibroManager(models.Manager):  # para hacer las consultas a la bbdd
    """managers para el modelo autor"""

    # def listar_autores(self):
    #   return self.all()  # el self nos trae lo que antes conociamos como autor.object
    # para decirle que esta clase ( AutorManager) pertenece a Autor, lo hace desde models

    def lista_libros1(self, kword):  # recibe un valor que es kword

        resultado = self.filter(
            titulo__icontains=kword,  # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
            # palabra que contenga el kword que recibe. LA COMA ES UN Y
            fecha__range=('2000-01-01', '2021-03-07')  # y que nos traiga los libros con este rango de fecha
        )

        return resultado

    # listar libros con el filtro TigreamSimilarity
    def lista_libros_trg(self, kword):  # recibe un valor que es kword

        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword
                # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
                # palabra que contenga el kword que recibe.

            )
            return resultado
        else:
            return self.all()[:10]

    def lista_libros2(self, kword, fecha1, fecha2):  # recibe el valor que es kword, y las fechas

        date1 = datetime.datetime.strptime(fecha1,
                                           '%Y-%m-%d').date()  # manera de convertir las fechas al formato deseado
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=kword,  # le decimos que el filtro (que sera filtrado por nombre) que busque cualquier
            # palabra que contenga el kword que recibe. LA COMA ES UN Y
            fecha__range=(date1, date2)  # y que nos traiga los libros con este rango de fecha
        )

        return resultado

    # Filtrado de categorias de un libro(es una FK)
    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria  # categoria__id, categoria es ela atributo que hace el fk
            # hace referencia en models en la class Libro, categoria= models.ForeignKey, que recoge entre sus datos id.
        ).order_by('titulo')

    # Agregar un nuevo autor a un determinado libro
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)  # recuperamos el libro cuyo id es igual al que le pasamos
        libro.autores.add(
            autor)  # ya tentemos el libro y queremos guardar un autor en su atributo "autores" que es muchos a muchos
        return libro

    # contar cuantas veces prestamos un libro orl aggregate
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado

    # Contar cuantas veces se ha prestado cada libro. no funciona porque no puede contar los mismos libros prestrados,
    # porque pertenecen a un resgistro( el de prestamo diferente ) video 135. hacerlo mejor desde libros.
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=Count('libro_prestamo')  # como estamos en la tablalibro y tenemos que accder a prestamo,
            # tenemos que utilizar la FK inversa de (models libor) related_name=libro_prestamo
        )
        for r in resultado:
            print("===================")
            print(r, r.num_prestados)

        return resultado


class CategoriaManager(models.Manager):
    """managers para el modelo categoria"""

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
            # categoria_libro es como se llama nuestro related_name de categorias que
            # es para poder hacer la relacion de con autor para sacar la info de de la categoria a la q pertence un autor
        ).distinct()  # con distinc me traigo las consultas q no se esten repitiendo

    # listar todas las categorias del sistema junto a la cantidad de libros por categoria
    def listar_categoria_libros(self):
        resultado = self.annotate(
            # Usamos annotate cuando queremos hacer una anotación en cada objeto que nos devuelva de un queryset
            num_libros=Count('categoria_libro')  # aqui cuento los libros que esta relacionado con la categoria traida
            # en annotate y como la relacion es de libros a categoria (fk), se utiliza su related_name='categoria_libro'
        )
        for r in resultado:
            print('***************')
            print(r, r.num_libros)
        return resultado
