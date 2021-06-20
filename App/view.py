﻿"""
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

def buscarCountry(catalog, country):
    # Se consulta si el país existe en la base de datos
    for x in range(1, lt.size(catalog['videos'])):
        if lt.getElement(catalog['videos'], x)['country'] == country:
            return True
        else:
            return False


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
            country = input('Ingrese el país deseado: ')
            if buscarCountry(catalog, country) == True:
                n_videos = int(input('Ingrese el número de videos que quiere listar: '))
            else:
                print('El país no existe')
        else:
            print('La categoría ingresada no existe')

        print('Cargando información de videos con más likes...')

    else:
        sys.exit(0)
sys.exit(0)
