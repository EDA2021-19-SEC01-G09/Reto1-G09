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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los IDs de categorías
    """
    catalog = {'videos': None,
               'categorias': None}

    catalog['videos'] = lt.newList()
    catalog['categorias'] = lt.newList('ARRAY_LIST'""",
                                    cmpfunction=compareauthors""")

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    #authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    #for cat in authors:
    #    addBookAuthor(catalog, author.strip(), book)

def addCategoria(catalog, categoria):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento