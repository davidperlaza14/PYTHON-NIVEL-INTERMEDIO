'''
listas_2.py
script en Python que calcula y muestra la suma de dos matrices cuadradas (misma cantidad de renglones y columnas)generadas aleatoriamente. Utilizar comprension de listas para generar las matrices de forma aleatoria.
'''
import random

N = 3

print(f"Programa que calcu;a la suma de matrices de tamano {N}x{N}")

m1 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
m2 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
resultado = [[0]*N for i in range(N)]

for renglon in range(N):
    for columna in range(N):
        resultado[renglon][columna] = m1[renglon][columna]+m2[renglon][columna]

print(m1)
print(m2)
print(resultado)