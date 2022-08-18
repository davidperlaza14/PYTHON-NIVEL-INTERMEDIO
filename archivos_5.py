'''
archivos_4.py
script en Python que genere un diccionario con las llaves siendo las extensiones unicas de los archivos encontrados en una carpeta y los valores una lista los nombres de cada uno de dichos archivos.
'''


import pathlib

def main():
    ruta = pathlib.Path('.')

    diccionario = {k : [v.name for v in ruta.glob(f'*{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}

    for extension, archivos in diccionario.items():
        print(f'extension: {extension}')
        print(f'archivo: {archivos}')

if __name__ == "__main__":
    main()