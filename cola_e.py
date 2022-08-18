# Crea una clase para representar la estructura de datos cola(queue) usando una lista.

class Cola:
    def __init__(self):
        self.datos = []

    def cantidad(self):
        return len(self.datos)

    def insertar(self, dato):
        self.datos.insert(0, dato)
    
    def extraer(self):
        if self.cantidad():
            return self.datos.pop()
        else:
            return None

    def primer_dato(self):
        if self.cantidad():
            return self.datos[-1]
    
    def ultimo_dato(self):
        if self.cantidad():
            return self.datos[0]


num = Cola()
num.insertar(2)
num.insertar(3)
num.insertar(4)
num.insertar(8)

print(num.primer_dato())
print(num.ultimo_dato())
print(num.cantidad())

print()

dato = num.extraer()
print(dato)
print(num.cantidad())

print()

num.extraer()
num.extraer()
num.extraer()
print(num.cantidad())

print()

dato = num.extraer()
print(dato)