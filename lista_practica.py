# Ejercicio Paractico con Listas
'''
Manipulacion de una lista
1. Capturar Lista
2. Mostar Lista
3. Agregar un Elemento a la Lista
4. Eliminar un Elemento de la Lista
5. Modificar un elemento de la lista
6. Salir
'''
import os
# Definiendo la funcion capturar
def capturar():
    global lista 
    lista = []
    print("Cuantos elementos va a tener la lista?")
    n = int(input())
    for i in range(0, n):
        print("Ingrese el elemento del indice ", i)
        elemento = input()
        lista.insert(i,elemento)

# Definiendo la funcion mostar
def mostrar():
    print(lista)

# Definiendo la funcion Agregar
def agregar():
    elemento = input("Ingresa el Elemento que deseas Agregar: ")
    indice = int(input("Ingresa el indice donde deseas Agregarlo: "))
    lista.insert(indice, elemento)
    print("Elemento Agregado")


# Definiendo la funcion Eliminar
def eliminar():
    indice = int(input("Ingresa el indice del elemento que deseas Eliminar: "))
    del lista[indice]
    mostrar()
    print("Elemento Eliminado")

# Definiendo la funcion Modificar
def modificar():
    indice = int(input("Ingresa el indice del elemento que deseas Modificar: "))
    elemento = input("Ingresa el nuevo elemento: ")
    lista[indice] = elemento
    print("Elemento Modificado")


# Definiendo la funcion main
def main():
    opcion = '1'
    while (opcion != 6):
        os.system
        print(f'''            Manipulacion lista\n
        1. Capturar Lista
        2. Mostar Lista
        3. Agregar un Elemento a la Lista
        4. Eliminar un Elemento de la Lista
        5. Modificar un elemento de la lista
        6. Salir
        
        ''')
        opcion = input('Elige una opcion: ')
        if opcion == '1':
            capturar()

        elif opcion == '2':
            mostrar()
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            eliminar()
        elif opcion == '5':
            modificar()
        elif opcion == '6':
            print("Has salido del menu.")
        else:
            ("Opcion incorrecta.")
            input("Enter para iniciar de nuevo.")
            
        input('Nos vemso...')

# Llamando a la funcion principal
main()