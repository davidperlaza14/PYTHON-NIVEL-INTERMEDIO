'''
archivios_2.py
script en Python que muestre los nombres de todos los archivos contenidos en una carpeta y que contenga una extencsion determinada.
'''

import pathlib

ruta =  pathlib.Path('.')

for archivo in ruta.glob('*.py'):
    print(archivo)