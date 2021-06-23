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

def newCatalog(tipo_lista):

    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorías
    """
    catalog = {'videos': None,
            'categorias': None}

    catalog['videos'] = lt.newList(tipo_lista)
    catalog['categorias'] = lt.newList(tipo_lista, cmpfunction = compararCategorias)
    
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

    

# Funciones de consulta

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
    if (int(video1['likes']) < int(video2['likes'])):
        return True

    # Funciones de ordenamiento

    def sortVideos(catalog, size, tipo_sort):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, cmpVideosByLikes)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
