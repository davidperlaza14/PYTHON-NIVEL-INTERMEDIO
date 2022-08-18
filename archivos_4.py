'''
archivos_4.py
script en Python que muestre todas las extensiones unicas de archivos existentes en una carpeta.
'''

from distutils import extension
import pathlib

def main():
    ruta = pathlib.Path(".")

    # for archivo in ruta.iterdir():
    #     print(archivo.suffix)

    extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f'extensiones: {extensiones}')


if __name__ == "__main__":
    main()