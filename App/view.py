"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar los libros por views")
    print("0- Salir")


def initCatalog(tad):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tad)


def loadData(catalog, tad):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog, tad)


def printResults(ord_books, sample):
    size = lt.size(ord_books)
    if size == sample:
        print("Los primeros ", str(sample), " libros ordenados son: ")
        i = 1
        while i <= sample:
            book = lt.getElement(ord_books, i)
            print('Titulo: ' + book['title'] + ' views: ' + book['views'])
            i += 1


def pregunta1():
    print("Seleccione la estructura de datos")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")


def pregunta2():
    print("Seleccione el metodo de ordenamiento")
    print("1- Selection Sort")
    print("2- Insertion Sort")
    print("3- Shell Sort")


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        pregunta1()
        tad = int(input())
        print("Cargando información de los archivos ....")
        new_type = None
        while new_type is None:
            if tad == 1:
                new_type = "ARRAY_LIST"
            elif tad == 2:
                new_type == "SINGLE_LINKED"
            else:
                print("No hizo una selección válida, por favor intente nuevamente a continuacion:\n")
        print(new_type)
        catalog = initCatalog(new_type)
        loadData(catalog[0], catalog[1])

        print('Videos cargados: ' + str(lt.size(catalog[0]['title'])))

        print('Nombres de canales cargados: ' +
              str(lt.size(catalog[0]['channel_title'])))

    elif int(inputs[0]) == 2:
        size = int(input("Indique el tamaño de la muestra: "))
        pregunta2()
        iterable_ord = int(input())

        new_order = None
        while new_order is None:
            if iterable_ord == 1:
                new_order = "selectionsort"
            elif iterable_ord == 2:
                new_order = "insertionsort"
            elif iterable_ord == 3:
                new_order = "shellsort"
            else:
                print("No hizo una selección válida, por favor intente nuevamente a continuacion:\n")

        result = controller.sortVideos(catalog, size, new_order)
        printResults(result[1], size)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))

    else:
        sys.exit(0)
sys.exit(0)
