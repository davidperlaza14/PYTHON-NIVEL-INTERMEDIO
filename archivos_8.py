'''
archivos_8.py
script en Python que solicite al una cantidad de peleiculas a registrar y los almacene en un archivo .csv (Comma Separated Value) para posteriormente recuperarlos. De cada pelicula se almacenara el titulo, la duracion y el año. 
'''
import os
import csv

def registrar_peliculas(nombre_archivo):
    cantidad = int(input('Cantidad de peliculas que desea registrar?: '))
    with open(nombre_archivo, 'a', newline='') as archivo_cvs:
        writer = csv.writer(archivo_cvs, delimiter=',')
        for i in range(cantidad):
            os.system("clear")
            titulo = input('Titulo: ')
            durracion = input('Duracion: ')
            año = input('año: ')
            writer.writerow([titulo, durracion, año])

def recuperar_peliculas(nombre_archivo):
    os.system('clear')
    print('Pleliculas registradas: ')
    with open(nombre_archivo, 'r', newline='') as archivo_cvs:
        reader = csv.reader(archivo_cvs)
        for linea in reader:
            print(f'Titulo: {linea[0]}')
            print(f'Duracion: {linea[1]}')
            print(f'año: {linea[2]}')
            print('~'*50)

def main():
    archivo = 'peliculas.csv'
    registrar_peliculas(archivo)
    recuperar_peliculas(archivo)


if __name__ == '__main__':
    main()