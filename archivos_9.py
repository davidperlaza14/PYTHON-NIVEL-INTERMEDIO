'''
archivos_8.py
script en Python que solicite al usuario una cantidad de peliculas a registrar
y los almacene en un archivo .csv con encabezados para posteriormente recuperarlos. De cada pelicula se almacenanar el titulo, la duracion y el año.
'''
from asyncore import write
import os
import csv
import pathlib

def registrar_peliculas(nombre_archivo):
    cantidad = int(input('Cuantas peliculas deseas registrar?: '))
    campos = ['Titulo', 'Duracion', 'Año']

    if not pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()

    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        for i in range(cantidad):
            os.system("clear")
            titulo = input('Titulo: ')
            duracion = input('Duracion: ')
            año = input('Año: ')
            writer.writerow({'Titulo':titulo, 'Duracion':duracion, 'Año':año})


def recuperar_peliculas(nombre_archivo):
    os.system('clear')
    print('Peliculas registradas')
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for liena in reader:
            for campo, valor in liena.items():
                print(f'{campo}: {valor}')
            print('*'*50)


def main():
    archivo = 'peliculas_encabezado.csv'
    registrar_peliculas(archivo)
    recuperar_peliculas(archivo)


if __name__ == '__main__':
    main()