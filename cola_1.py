'''
                    COLA
Criterio: First in first Out (FIFO)
El primer dato en entrar es el primero en salir.
'''
'''
cola_1.py
script en Python que permita al usuario registrar eventos en su agenda; cada evento se agregara en una cola de prioridad de la estructura. Para manejar la agenda se le mostrara al usuario un menu con las opciones agregar evento y atender evento.
'''

import os
import queue

AGENDAR = 1
ATENDER = 2
SALIR = 0

def mostrar_menu():
    os.system("clear")
    print(f'''                  Mi Agenda
{AGENDAR}) Agendar evento
{ATENDER}) Atender evento
{SALIR}) Salir''')

def agregar_evento(ag):
    print('                     Agregar Evento')
    evento = input('Evento: ')
    ag.put(evento)

def atender_evento(ag):
    print('                     Atender Evento')
    if ag.empty():
        print('No hay eventos por atender')
    else:
        evento = ag.get()
        print(f'Evento: {evento}')

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opcion: '))
        os.system('clear')
        if opc == AGENDAR:
            agregar_evento(agenda)
        elif opc == ATENDER:
            atender_evento(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida...')
        input('Presione enter para continuar')
print("Nos vemos...")


if __name__ == "__main__":
    main()