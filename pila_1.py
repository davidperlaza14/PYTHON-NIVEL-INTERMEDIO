'''
PILA
Criterio: Last In First Out (LIFO)
El ultimo dato en entrar es el primero en salir
'''

'''
pila_1.py
script en python que solicite al usuario una expresion aritmetrica y el programa le indique si dicha expresion esta balanceada,  es decir, si tiene la misma cantidad de parentesisis de apertura y de cierre.
'''



def validar_expresion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == "(":
            pila.append("(")
        elif simbolo == ")":
            if len(pila) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0

def main():
    print("Escribe una expresion aritmetica y te indicare si esta bien con respecto a parentesis")
    e = input("Expresion: ")
    valida = validar_expresion(e)
    if valida:
        print("La expresion esta balanceada")
    else:
        print("La expresion no esta balanceada")
    input("Nos vemos...")

if __name__ == "__main__":
    main()