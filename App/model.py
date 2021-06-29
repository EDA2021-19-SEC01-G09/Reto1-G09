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
from DISClib.Algorithms.Sorting import selectionsort as sn
from DISClib.Algorithms.Sorting import insertionsort as nn
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms

assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorías
    """
    catalog = {'videos': None,
            'categorias': None}

    catalog['videos'] = lt.newList("ARRAY_LIST")
    catalog['categorias'] = lt.newList("ARRAY_LIST", cmpfunction = compararCategorias)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)

def addCategoria(catalog, categoria):
    """
    Adiciona un tag a la lista de tags
    """
    lt.addLast(catalog['categorias'], categoria)

# Funciones para creacion de datos

def buscarCategoria(catalog, categoria):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    if lt.isPresent(catalog['categorias'], categoria) > 0:
        return True
    else:
        return False

def filtrarRequerimiento1(catalog, categoria, country):
    listaFiltrada = lt.newList()
    for i in range(0, lt.size(catalog['videos'])):
        elementos = lt.getElement(catalog['videos'], i)
        if elementos['category_id'] == categoria and elementos['country'] == country:
            lt.addLast(listaFiltrada, elementos)
    return listaFiltrada

def filtrarRequerimiento3(catalog, categoria):
    listaFiltrada = lt.newList()
    for i in range(0, lt.size(catalog['videos'])):
        elementos = lt.getElement(catalog['videos'], i)
        likes = int(elementos['likes'])
        dislikes = int(elementos['dislikes'])
        if dislikes == 0:
            dislikes = 1
        if elementos['category_id'] == categoria:
            if elementos['dislikes']: 
                if int(elementos['likes']) / int(elementos['dislikes']) > 20:
                    elementos['frec'] = 1
                    lt.addLast(listaFiltrada, elementos)
    return listaFiltrada


# Funciones de consulta

def buscarPais(catalog, pais): 
    falso = False
    for i in range(0, lt.size(catalog['videos'])):
        elemento = lt.getElement(catalog['videos'],i)
        verificar = (elemento['country'] == pais)
        if verificar == True:
            falso = True
            break
    return falso


# Funciones utilizadas para comparar elementos dentro de una lista

def compararCategorias(categoria1, categoria):
    if categoria1.lower() in categoria['name'].lower():
        return 0
    return -1

def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los likes de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'likes'
        video2: informacion del segundo video que incluye su valor 'likes'
    """
    if (int(video1['likes']) > int(video2['likes'])):
        return True

    # Funciones de ordenamiento

def sortVideos(catalog, size):
    sub_list = lt.subList(catalog, 1, lt.size(catalog))
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpVideosByLikes)    
    sub_list2 = lt.subList(sorted_list, 1, size)
    return sub_list2


