'''
diccionario_1.py
script en Python que implemente una agenda de contactos haciendo uso de un diccionario. Para el diccionario las llaves seran los nombre de los contactos y como valor estara una tupla que contenga el numero telefonico y el correo electronico. se tendra un menu con las siguientes opciones:

1) Agregar contacto
2) Mostarar contacto
3) Buscar contacto
4) Modificar contacto
5) Eliminar contacto
0) Salir
'''
import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5

def mostrar_menu():
    os.system("clear")
    print(f'''                  Mi Agenda
{AGREGAR}) Agregar contacto
{MOSTRAR}) Mostarar contacto
{BUSCAR}) Buscar contacto
{MODIFICAR}) Modificar contacto
{ELIMINAR}) Eliminar contacto
{SALIR}) Salir''')

def agregar_contacto(agenda):
    os.system("clear")
    print('                     Agregar contacto')
    nombre = input("Nombre: ")
    if agenda.get(nombre):
        print("Ya existe el contacto")
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        agenda.setdefault(nombre, (telefono, email))
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
    os.system('clear')
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

def modificar_contacto(agenda):
    os.system("clear")
    print('                         Modificar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print('Informacion actual: ')
            print(f'Nombre: {nombre}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('*'*50)
            print('Ingrese los nuevos datos: ')
            telefono = input('Telefono: ')
            email = input('Email: ')
            agenda[nombre] = (telefono, email)
            print('Datos actualizados con exitos.')            
        else:
            print('No existe ningun dato')
    else:
        print('No hay contactos registrados.')

def eliminar_contacto(agenda):
    os.system("clear")
    print('                         Eliminar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            agenda.pop(nombre)
            print('Contacto eliminado con exito.')
        else:
            print('No existe el contacto.')
    else:
        print('No hay contactos registrados.')


def main():
    continuar = True
    mi_agenda = {}
    while continuar:
        mostrar_menu()
        opc  = int(input('Selecciona una opcion:  '))

        if opc == AGREGAR:
            agregar_contacto(mi_agenda)
        elif opc == MOSTRAR:
            mostrar_contactos(mi_agenda)
        elif opc  == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == MODIFICAR:
            modificar_contacto
        elif opc == ELIMINAR:
            eliminar_contacto(mi_agenda)
        elif opc  == SALIR:
            continuar = False
        else:
            print('Opcion no valida.')
        input('Presiona enter para continuar...')
    print('Nos vemos...')

if __name__ == '__main__':
    main()