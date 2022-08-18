'''
Escribe un programa que le pregunte al usuario su nombre, edad, direccion y telefono y lo guarde en un diccionario. Despues debe mostrar por pantalla el mensaje
'''

nombre = input('Tu nombre: ')
edad = input('Tu edad: ')
direccion = input('Tu direccion: ')
telefono = input('Escribe tu numero de telefono: ')

datos_usuarios = {
    'nombre': nombre,
    'edad' : edad,
    'direccion' : direccion,
    'telefono' : telefono
}

print(f"{datos_usuarios['nombre']} tiene {datos_usuarios['edad']} años, vive en {datos_usuarios['direccion']} su tel es: {datos_usuarios['telefono']}")