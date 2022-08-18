'''
tuplas_1.py
script en Python que permita almacenar registros de las mascotas del usuario. Para cada mascota se solicitara el nombre, la edad, el peso, y el tipo de mascota; dichos valores seran guardados en una tupla. Para permitir la posibilidad de tener varias mascotas se creara una lista en la cual se guarden los registros de cada mascota, es decir una lista de tuplas. El programa debera contar con un menu ciclico que permita registrar y consultar las mascotas.
'''

import os

REGISTRAR = 1
CONSULTAR = 2
SALIR = 0

def mostar_menu():
    os.system("clear")
    print(f'''                  Mis Mascotas
{REGISTRAR}) Registrar una mascota
{CONSULTAR}: Consultar mascotas
{SALIR}) Salir''')

def registrar_mascotas(mascotas):
    print('                     Registrar Mascotas')
    nombre = input("Nombre: ")
    edad = int(input('edad: '))
    peso = float(input("Peso: "))
    tipo = input("Tipo: ")
    mascotas.append( (nombre, edad, peso, tipo) )

def consultar_mascotas(mascotas):
    os.system('clear')
    print('                     Mis Mascotas')
    if len(mascotas) == 0:
        print('Aun no has registrado mascotas')
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f'Nombre: {nombre}')
            print(f'Edad: {edad}')
            print(f'Peso: {peso}')
            print(f'Tipo: {tipo}')
            print(' ^.^ ´0.0`'*8)

def main():
    mis_mascotas = []
    continuar = True
    while continuar:
        mostar_menu()
        opc = int(input('Seleccionar una opcion: '))
        if opc == REGISTRAR:
            registrar_mascotas(mis_mascotas)
        elif opc == CONSULTAR:
            consultar_mascotas(mis_mascotas)
        elif opc == SALIR:
            continuar = False
        else : 
            print("Opcion no valida")
        input("Presiona enter para continuar...")
    input("Nos vemos...")


if __name__ == "__main__":
    main()