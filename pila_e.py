'''
Ejercicio con pila en Python
'''

import os
from traceback import print_last

pila = []
cima = -1

while True:

    print("Menu")
    print("Selecciona una opcion")
    print("[1] Meter datos")
    print("[2] Sacar datos")
    print("[3] Pila vacia?")
    print("[4] Mostrar pila")
    print("[5] Salir")
    opc = input(" ")
    if opc == '1':
        if cima < 5:
            pila.append(input('Introdusca dato'))
            cima += 1
        else:
            print("La pila esta llena")
    elif opc == "2":
        if cima > -1:
            print(pila.pop())
            cima -= 1
        else:
            print("La pila esta vacia, por favor introducir un dato antes.")
    elif opc == "3":
        if cima == -1:
            print("La pila esta vacia")
        else:
            print("La pila no esta vacia")
    elif opc == "4":
        if cima != -1:
            print(pila)
        else:
            print("La pila esta vacia")
    elif opc == "5":
        break
    else:
        print("Opcion invalida, intenta de nuevo.")