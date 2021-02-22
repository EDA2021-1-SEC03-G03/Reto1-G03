"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    catalog = {'title': None,
               'channel_title': None}

    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList('ARRAY_LIST',
                                          cmpfunction=compareauthors)

    return catalog


def addVideo(catalog, title):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['title'], title)
    # Se obtienen los autores del libro
    authors = title['channel_title'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for channel in authors:
        addTitleChannel(catalog, channel.strip(), title)


def addTitleChannel(catalog, authorname, title):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['channel_title']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['title'], title)


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos


def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "title": None}
    author['name'] = name
    author['title'] = lt.newList('ARRAY_LIST')
    return author

# Funciones de consulta


def getVideosByChannel(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posauthor = lt.isPresent(catalog['channel_title'], authorname)
    if posauthor > 0:
        author = lt.getElement(catalog['channel_title'], posauthor)
        return author
    return None


def getBestVideos(catalog, number):
    """
    Retorna los mejores libros
    """
    videos = catalog['title']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos

# Funciones utilizadas para comparar elementos dentro de una lista


def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(catalog, size):
    sub_list = lt.subList(catalog['title'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
