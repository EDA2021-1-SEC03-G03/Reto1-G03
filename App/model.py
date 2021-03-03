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
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as shs

assert cf

# Construccion de modelos


def newCatalog(tad):
    catalog = {'title': None,
               'channel_title': None}

    catalog['title'] = lt.newList(tad)
    catalog['channel_title'] = lt.newList(tad,
                                          cmpfunction=compareChannelTitle)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, title):
    lt.addLast(catalog['title'], title)

# Funciones para creacion de datos

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
    sub_list = lt.subList(catalog['title'], 0, size)
    if iterable_ord == "quicksort":
        new_title = qs.sort(sub_list, cmpVideosByViews)
    elif iterable_ord == "mergesort":
        new_title = ms.sort(sub_list, cmpVideosByViews)
    elif iterable_ord == "selectionsort":
        new_title = ss.sort(sub_list, cmpVideosByViews)
    elif iterable_ord == "insertionsort":
        new_title = ins.sort(sub_list, cmpVideosByViews)
    elif iterable_ord == "shellsort":
        new_title = shs.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, new_title
