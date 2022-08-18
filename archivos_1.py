'''
                    Archivos

open(nimbre_archivo,modo)
'r' - lectura
'w' - escritura
'a' - agregar
'r+' - lectura y escritura
'b' - binario
'''

'''
Filtrar y bbuscar archivos

archivos_1.py
script enPython que muestre el nombre de todos los archivos contenidos en una carpeta.
'''
import pathlib 

ruta = pathlib.Path('.')

for archivo in ruta.iterdir():
    print(archivo)
