'''
Listas_e.py
script en Python que implemente el clasico juego de "Ahorcado".
El juego consiste en que el usuario intente adivinar una palabra
secreta de la cual inicialmente solo se le muestra la cantidad
de letras que contiene. Para esta version del juego, el usuario
debera intentar adivinar e el nombre de alguno de los 35 paises
que conforman el continente americano.

El juego debe que comenzar seleccionando de forma aleatoria el 
nombre de alguno de los paises; dichos nombres deberan estar 
almacenados en una lista. Una vez seleccionado el pais, se le
mostrara al usuario una cadena formada por tantos guiones bajos
como letras y  espacios en blanco haya  en el nombre del pais.
Por ejemplo si el pais es "Cuba", al asuario se le mostraria
"____" (4 guiones bajos).

A partir  de ahi el usuario debe intentar adivinar las letras
que conforman el nombre teniendo hasta 5 oportunidades para
fallar.
'''

import os
import random

MAX_FALLOS = 5

paises =  ['Argentina','Bolivia','Brasil','Chile','Colombia','Ecuador','Guyana','Guyana Francesa',
'Paraguay','Perú','Suriname','Uruguay','Venezuela']

def crear_cadenas():
    pais = random.choice(paises)
    secreto = "-"*len(pais)
    return pais, secreto

def reemplazar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos+1:]
        inicio = pos + 1
    return secreto

def ahorcado():
    print(f"Juego del Ahorcado. Adivina el nombre de los paises  {len(paises)} paises de Sur America. Tu numero de vidas seran {MAX_FALLOS}. Comencemos!!")
    input("Presiona enter para comenzar")
    original, secreto = crear_cadenas()
    fallos = 0
    while secreto != original and fallos < MAX_FALLOS:
        os.system("clear")
        print(f"Palabra: {secreto}")
        s = input("Cual simbolo quieres destapar?: ")
        if s in original:
            secreto = reemplazar_simbolo(original, secreto, s)
            print("Bien hecho!")
        else:
            print("Lo siento, la letra no es parte de la palabra.")
            fallos += 1
            print(f"Llevas un total de {fallos} fallos")
        input("Presiona enter para continuar...")
    os.system("clear")
    if secreto == original:
        print(f"Felicidades, el pais es {secreto}")
    else:
        print(f"Lo siento, el pais es {secreto}")
    print(" Nos vemos...")


def main():
    ahorcado()

if __name__ == "__main__":
    main()