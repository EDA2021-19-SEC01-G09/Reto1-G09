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
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Cargar videos con más likes en función de país y categoría")
    print("3- Cargar vídeo con percepción altamente positiva con más días siendo tendencia en función de país")
    print("4- Cargar vídeo con percepción sumamente positiva con más días siendo tendencia en función de categoría")
    print("5- Cargar vídeos con más comentarios en función de país y tag específico")

# InitCatalog (llama al modelo desde el controlador)
# LoadData (Solo existe en controller y llama a otras funciones allí)
def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def filtrarCatalogo(catalog):
    """
    filtra el primer video 
    """
    newDict = dict()
    for (key, value) in lt.firstElement(catalog['videos']).items():
            # Check if key is even then add pair to new dictionary
        if key in ['title', 'channel_title', 'trending_date', 'country', 'views', 'likes', 'dislikes']:
                newDict[key] = value
    return newDict

def iterarCategorias(catalog):
    """
    Imprime todas las cateregorías en forma de diccionario en diferentes lineas
    """
    for x in range(1, lt.size(catalog['categorias'])):
        categoria = lt.getElement(catalog['categorias'], x)
        print(categoria)

def iterarOrg(lista):
    """
    Imprime todas las cateregorías en forma de diccionario en diferentes lineas
    """
    for x in range(1, lt.size(lista[1])):
        y = lt.getElement(lista[1], x)
        print(y)
    
def obtenerIdCategoria(catalog, category_name):
    for i in range(0, lt.size(catalog['categorias'])):
        categoriaDada = lt.getElement(catalog['categorias'], i)
        if category_name == categoriaDada['name']:
            return categoriaDada['id']

def printResultsReq1(ord_videos, n_videos):
    size = lt.size(ord_videos)
    if size >= n_videos:
        print("Los ", n_videos, " videos con más likes son: ")
        i = 1
        while i <= (n_videos):
            video = lt.getElement(ord_videos, i)
            print('Trending date: ' + video['trending_date'] + ' Título: ' +
            video['title'] + ' Nombre del canal: ' + video['channel_title'] + ' Fecha publicación: ' + video['publish_time'] + ' Vistas: ' + video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: ' + video['dislikes'])
            i += 1
    return ""

def printResultsReq2(ord_videos):
    video = lt.getElement(ord_videos, 1)
    print('País: ' + video['country'] + ' Título: ' + video['title'] + ' Nombre del canal: ' + video['channel_title'] + ' Relación likes/dislikes: ' + str(video['ratio_likes_dislikes']) + ' Días: ' + str(video['dias']))      
    return ""

def printResultsReq3(ord_videos):
    video = lt.getElement(ord_videos, 1)
    print('Categoría: ' + video['category_id'] + ' Título: ' + video['title'] + ' Nombre del canal: ' + video['channel_title'] + ' Relación likes/dislikes: ' + str(video['ratio_likes_dislikes']) + ' Días: ' + str(video['dias']))      
    return ""

def printResultsReq4(ord_videos, n_videos):
    size = lt.size(ord_videos)
    if size >= n_videos:
        print("Los ", n_videos, " videos con más comentarios son: ")
        i = 1
        while i <= (n_videos):
            video = lt.getElement(ord_videos, i)
            print('Comentarios: ' + video['comment_count'] + ' Título: ' +
            video['title'] + ' Nombre del canal: ' + video['channel_title'] + ' Fecha publicación: ' + video['publish_time'] + ' Vistas: ' + video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: ' + video['dislikes'] + ' Tags: ' + video['tags'])
            i += 1
    return ""
   
catalog = None


"""
Menu principal
"""


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos']))) 
        print('Filtered Dictionary: ')
        print(filtrarCatalogo(catalog))
        print('Categorías cargadas: ')
        iterarCategorias(catalog)

    elif int(inputs[0]) == 2:
        category_name = input('Ingrese la categoría deseada: ')
        if controller.buscarCategoria(catalog, category_name) == True:
            id = obtenerIdCategoria(catalog, category_name)
            country = input('Ingrese el país deseado: ')

            if controller.buscarPais(catalog, country) == True:
                listaFiltrada = controller.filtrarRequerimiento1(catalog, id, country)
                print("Se cargaron ", lt.size(listaFiltrada))
                n_videos = int(input('Ingrese el número de videos que quiere listar: '))

                if n_videos > lt.size(listaFiltrada):
                    print('La sublista deseada excede el número de elementos cargados. Por favor ingresar otro valor.')

                else:
                    result = controller.sortVideos(listaFiltrada, n_videos)
                    print('Cargando información de videos con más likes...')
                    print(printResultsReq1(result, n_videos))

            else:
                print('El país no existe')
        else:
            print('La categoría ingresada no existe')

    elif int(inputs[0]) == 3:
        country = input('Ingrese el pais deseado: ')
        if controller.buscarPais(catalog, country) == True:
            listaFiltrada = controller.filtrarRequerimiento2(catalog, country)
            print("Se cargaron ", lt.size(listaFiltrada))
            result = controller.sortDias(listaFiltrada)
            print(printResultsReq2(result))
        else:
            print('El país ingresado no existe.')

    elif int(inputs[0]) == 4:
        category_name = input('Ingrese la categoría deseada: ')
        if controller.buscarCategoria(catalog, category_name) == True:
            id = obtenerIdCategoria(catalog, category_name)
            listaFiltrada = controller.filtrarRequerimiento3(catalog, id)
            print("Se cargaron ", lt.size(listaFiltrada))
            result = controller.sortDias(listaFiltrada)
            print(printResultsReq3(result))
        else:
            print('La categoría ingresada no existe.')
        
    elif int(inputs[0]) == 5:
        country = input('Ingrese el pais: ')
        if controller.buscarPais(catalog, country) == True:
            tag = str(input('Ingrese el tag: '))

            if controller.buscarTag(catalog, tag) == True:
                listaFiltrada = controller.filtrarRequerimiento4(catalog, country, tag)
                print("Se cargaron ", lt.size(listaFiltrada))
                n_videos = int(input('Ingrese el número de videos que quiere listar: '))

                if n_videos > lt.size(listaFiltrada):
                    print('La sublista deseada excede el número de elementos cargados. Por favor ingresar otro valor.')

                else:
                    result = controller.sortComentarios(listaFiltrada, n_videos)
                    print('Cargando información de videos con más likes...')
                    print(printResultsReq4(result, n_videos))
            else:
                print('El tag no existe')
        else:
            print('El país no existe.')


    else:
        sys.exit(0)
sys.exit(0)
