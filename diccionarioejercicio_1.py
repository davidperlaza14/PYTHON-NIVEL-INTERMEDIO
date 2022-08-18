divisas = { 
    'Euro':'€', 
    'Dolar':'$',
    'Yen':'¥'
}

divisa = input('Escribe una divisa: ')
if divisas.get(divisa):
    print(divisas.get(divisa))
else:
    print('La divisa no esta.')