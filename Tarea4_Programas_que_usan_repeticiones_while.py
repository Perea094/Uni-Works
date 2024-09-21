# Diego Perea León
# A01708350
# Tarea 4

import random

YES = ['Si', 'si', 'sí', 's', 'S', 'Sí', 'SI', 'SÍ', 'yes', 'YES']
NO = ['No', 'NO', 'no', 'n', 'N']


def valor(x):
    while True:
        try:
            w = float(input(x))
            return w
        except ValueError:
            print("Introduce un número")


def sino():
    while True:
        bucle = input('Desea repetir el programa?\t')
        if bucle in YES:
            print("Ingresaste 'Sí'")
            return True
        elif bucle in NO:
            print("Ingresaste 'No'")
            return False
        else:
            print("Entrada no válida")


def main():
    numero_aleatorio = random.randint(1, 100)
    while True:
        valor_usuario = valor('Introduzca un valor: \t')
        if valor_usuario < numero_aleatorio:
            print('El número es menor')
        elif valor_usuario > numero_aleatorio:
            print('El número es mayor')
        else:
            print('Excelente, lo ha adivinado')
            break


def iniciar():
    while True:
        main()
        if not sino():
            break


iniciar()
