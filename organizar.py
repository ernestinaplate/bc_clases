import csv
import math
from random import randint

with open('people.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

# for i in range(1,len(your_list)):
    # print(your_list[i][2], your_list[i][3])

def formatear_cvs(cvs):
    lista_parcial = []
    for i in range(1,len(cvs)):
        nuevo_elemento = str(cvs[i][2]) + " " + str(cvs[i][3])
        lista_parcial.append(nuevo_elemento)
    return lista_parcial

def crear_grupos(lista_participantes, integrantes, tipo):
    contador = 1
    organizacion = []
    while len(lista_participantes) >= integrantes:
        grupo = []
        for i in range(integrantes):
            largo = len(lista_participantes) - 1
            index = randint(0, largo)
            integ = lista_participantes[index]
            grupo.append(integ)
            lista_participantes.pop(index)
        organizacion.append(grupo)
    if len(lista_participantes) == 0:
        return organizacion
    elif tipo == "1":
        for i in range(len(lista_participantes)):
            participante = lista_participantes[i]
            var = len(organizacion) - 1
            organizacion[var].append(participante)
        return organizacion
    else:
        nuevo_grupo = []
        for i in range(len(lista_participantes)):
            nuevo_grupo.append(lista_participantes[i])
        organizacion.append(nuevo_grupo)
        return organizacion

def imprimir_grupos(lista_grupos):
    for i in range(len(lista_grupos)):
        print("Grupo " + str(i+1))
        print(lista_grupos[i])


cant_por_grupo = input("Inserte la cantidad de integrantes por grupo: ")
int_grupo = int(cant_por_grupo)
tipo = input("La organizacion debe ser por (1) exceso o por (2) defecto? ")
participantes_format = formatear_cvs(your_list)
agrupacion = crear_grupos(participantes_format, int_grupo, tipo)
imprimir_grupos(agrupacion)