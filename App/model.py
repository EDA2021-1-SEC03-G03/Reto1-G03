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
from DISClib.Algorithms.Sorting import insertionsort as so
from DISClib.Algorithms.Sorting import selectionsort as su
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos 
listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tad):
    catalog = {'title': None,
               'channel_title': None}

    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList(tad,
                                          cmpfunction=compareChannelTitle)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, title, tad):
    lt.addLast(catalog['title'], title)
    channel_title = title['channel_title'].split(",")
    for channel in channel_title:
        addTitleChannel(catalog, channel.strip(), title, tad)


def addTitleChannel(catalog, channel_title, title, tad):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channles = catalog['channel_title']
    poschannel = lt.isPresent(channles, channel_title)
    if poschannel > 0:
        channel = lt.getElement(channles, poschannel)
    else:
        channel = newChannelTitle(channel_title, tad)
        lt.addLast(channles, channel)
    lt.addLast(channel['title'], title)

# Funciones para creacion de datos


def newChannelTitle(name, tad):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    channel = {'name': "", "title": None, 'views': 0}
    channel['name'] = name
    channel['title'] = lt.newList(tad)
    return channel

# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista


def compareChannelTitle(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento
def sortVideos(catalog, size, iterable_ord):
    start_time = time.process_time()
    sub_list = lt.subList(catalog[0]['title'], 0, size)
    if iterable_ord == "selectionsort":
        new_title = su.sort(sub_list, cmpVideosByViews)
    elif iterable_ord == "insertionsort":
        new_title = so.sort(sub_list, cmpVideosByViews)
    elif iterable_ord == "shellsort":
        new_title = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, new_title
