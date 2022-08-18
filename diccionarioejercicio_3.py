'''
Escribe un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un numero de kilos y muestre por pantalla el precio de ese numero de kilo de fruta. Si la fruta no esta en el diccionario debe mostrar un mensaje informando de ello.

                    Fruta     Precio
                    Platano    1.35
                    Manzana    0.80
                    Pera       0.85
                    Naranja    0.70

'''
frutas = {
    'platano' : 1.35,
    'manzana' : 0.80,
    'pera' : 0.85,
    'naranja' : 0.70
}

fruta = input('Que fruta deseas?: ')

if fruta in frutas:
    kilos = float(input(f'Cuantos kilos de {fruta} quieres?: '))
    print(f'{kilos} kilos de {fruta} cuestan ${frutas[fruta]*kilos}')
else:
    print(f'{frutas} no se encuentra disponible.')