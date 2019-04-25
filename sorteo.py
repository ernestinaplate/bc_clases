from random import randint

partic = input("Inserte la cantidad de participantes en el sorteo: ")
int_partic = int(partic)
premios = input("Inserte la cantidad de premios: ")
int_premios = int(premios)


def agregar_lista(cant_partic):
    lista_partic = []
    print("Inserte los participantes:")
    for i in range(cant_partic):
        nuevo_nombre = input()
        lista_partic.append(nuevo_nombre)
    return lista_partic

def sorteo(lista, cant_premios):
    lista_ganadores = []
    for i in range(cant_premios):
        index_ganador = randint(0,(len(lista)-1))
        ganador = lista[index_ganador]
        lista_ganadores.append(ganador)
        lista.pop(index_ganador)
    return lista_ganadores

def imprimir_ganadores(lista_ganadores):
    print("Los ganadores son:")
    for i in range(len(lista_ganadores)):
        print(lista_ganadores[i])

partic_final = agregar_lista(int_partic)
ganadores = sorteo(partic_final, int_premios)
# print("La lista de participantes es:\n" + str(partic_final))
print("Se realiza el sorteo.")
imprimir_ganadores(ganadores)
