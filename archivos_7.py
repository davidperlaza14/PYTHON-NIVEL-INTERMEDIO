'''
archivos_7.py
diccionario_1.py
script en Python que implemente una agenda de contactos haciendo uso de un diccionario. Para el diccionario las llaves seran los nombre de los contactos y como valor estara una tupla que contenga el numero telefonico y el correo electronico. se tendra un menu con las siguientes opciones:

1) Agregar contacto
2) Mostarar contacto
3) Buscar contacto
0) Salir
'''
import email
from importlib.resources import path
import pathlib
import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3

def mostrar_menu():
    os.system("clear")
    print(f'''                  Mi Agenda
{AGREGAR}) Agregar contacto
{MOSTRAR}) Mostarar contacto
{BUSCAR}) Buscar contacto
{SALIR}) Salir''')

def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefault(contacto,(telefono, email))
    else:
        with open(nombre_archivo, 'w') as archivo:
            pass

def agregar_contacto(agenda, nombre_archivo):
    os.system("clear")
    print('                     Agregar contacto')
    nombre = input("Nombre: ")
    if agenda.get(nombre):
        print("Ya existe el contacto")
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        agenda.setdefault(nombre, (telefono, email))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f'{nombre}, {telefono},{email}\n')
        print('Contacto agregado con exito.')

def mostrar_contactos(agenda):
    os.system('clear')
    print('                     Mis contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('~'*50)
    else:
        print('No hay contactos registrados')

def buscar_contacto(agenda):
    os.system("clear")
    print('                     Buscar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                print('~'*50)
                encontrados += 1
        if encontrados == 0:
            print('No se encontro el contacto.')
        else:
            print(f'Se encontraron {encontrados} contactos.')
    else:
        print('No hay contactos registrados.')


def main():
    continuar = True
    agenda = dict()
    nombre_archivo = 'agenda.txt'
    cargar_agenda(agenda, nombre_archivo)

    while continuar:
        mostrar_menu()
        opc  = int(input('Selecciona una opcion:  '))

        if opc == AGREGAR:
            agregar_contacto(agenda, nombre_archivo)
        elif opc == MOSTRAR:
            mostrar_contactos(agenda)
        elif opc  == BUSCAR:
            buscar_contacto(agenda)
        elif opc  == SALIR:
            continuar = False
        else:
            print('Opcion no valida.')
        input('Presiona enter para continuar...')
    print('Nos vemos...')

if __name__ == '__main__':
    main()