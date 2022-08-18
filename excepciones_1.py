'''
excepciones?1.py
script de Python que muestre un menu con distintos personajes de un videojuego. Si el usuario selecciona uno de los personajes, se le mostrara sus caracteristicas. El menu sera ciclico y se mostrara mientras el usuario no indique que desea salir.
'''

import os


MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 4

#bandera
continuar = True

while continuar:
    os.system("clear")
    print(f"""                              Personajes
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir
    """)
    opc = input("Slecciona tu personaje: ")
    try:
        opc = int(opc)
    except:
        opc = -1

    if opc == MAGO:
        print("""
        Fuerza: 15
        Energia: 20
        Especial: 12
        """)
    elif opc == GUERRERO:
        print("""
        Fuerza: 25
        Energia: 18
        Especial: 10
        """)
    elif opc == SACERDOTISA:
          print("""
        Fuerza: 18
        Energia: 25
        Especial: 22
        """)
    elif opc == SALIR:
       continuar = False
    else:
        print("Opcion no validas")
    input("Presiona enter para continuar")
input("Nos vemos...")