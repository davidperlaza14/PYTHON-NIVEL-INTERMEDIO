'''
Ejercicio 5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
'''

asignaturas = {
    'Matemáticas': 7, 'Física': 7, 'Química': 7

}

total_creditos = 0

for asignatura in asignaturas:
    print(f'{asignatura} tiene {asignaturas[asignatura]} de creditos')
    total_creditos += asignaturas[asignatura]
print(f'Total de creditos: {total_creditos}')