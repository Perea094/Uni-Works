# Diego Perea León A01708350

# Pedir piedra papel o tijera

import random


def dato(x):
    while True:
        try:
            w = int(input(x))
            if w in [1, 2, 3, 4]:
                return w
            else:
                print("Por favor, ingrese un número dentro del rango.")
        except ValueError:
            print('Ingrese un número entero positivo')


def tiro(tiropc):
    if tiropc == 1:
        return 'Piedra'
    elif tiropc == 3:
        return 'Tijera'
    elif tiropc == 2:
        return 'Papel'


def func(x1, y1):
    v1 = str(x1) + str(y1)
    return v1


def ganador(gano):
    if gano == '12' or gano == '23' or gano == '31':
        return 'Gana Computador'
    elif gano == '13' or gano == '21' or gano == '32':
        return 'Gana Usuario'
    elif gano == '11' or gano == '22' or gano == '33':
        return 'Empate'


def combat(x, y, z):
    print(f"Tiro compu: {tiro(x)}")
    print(f"Tiro usuario: {tiro(y)}")
    win = ganador(z)
    print(f"¡{win}!")
    return False


def desarrollo():
    while True:
        tiro_usuario = dato("\n1.\tPiedra\n2.\tPapel\n3.\tTijeras\n4.\tSalir\n")
        tiro_compu = random.randint(1, 3)
        v2 = func(tiro_usuario, tiro_compu)
        combat(tiro_compu, tiro_usuario, v2)
        if tiro_usuario == 4:
            break


desarrollo()
