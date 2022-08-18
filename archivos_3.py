'''
archivos_3.py
script en Python que busque un archivo en una carpeta e idique si existe o no. En caso de existir mostrar su tamaño.
'''

import pathlib

ruta = pathlib.Path('.')

print('Programa que busca un archivo dentro de la carpeta de trabajo')
archivo = input('Nombre del archivo buscado: ')
archivo = ruta / archivo

if archivo.exists():
    print(f'El archivo existe y mide {archivo.stat().st_size} bytes.')
else:
    print('No existe el archivo.')