'''
ejercicio_4.py
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato  dd de <mes> de aaaa donde <mes> es el nombre del mes.
'''
meses = {
    '1' : 'Enero',
    '2' : 'Feb',
    '3' : 'Mar',
    '4' : 'Abr',
    '5' : 'May',
    '6' : 'Jun',
    '7' : 'Jul',
    '8' : 'Ago',
    '9' : 'Sep',
    '10' : 'Oct',
    '11' : 'Nom',
    '12' : 'Dic'
 }

fecha = input('Escribe una fecha en formato dd/mmm/aaaa: ')
fecha = fecha.split('/')
print(f'{fecha[0]} / {meses[fecha[1]]} / {fecha[2]}')