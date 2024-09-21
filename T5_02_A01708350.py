# Diego Perea León A01708350
# Cuenta Regresiva
# Ejercicio 2

import time


def dato(x):
    while True:
        try:
            w = int(input(x))
            if w > 0:
                return w
            else:
                print("Por favor, ingrese un numero entero positivo")
        except ValueError:
            print("Por favor, ingrese un numero entero positivo")


def cuentaRegresiva(x):
    while x >= 0:
        print(x)
        time.sleep(1)
        x -= 1
    return x


def registro():
    segundos = cuentaRegresiva(dato('Ingrese una cantidad en segundos para iniciar la cuenta regresiva:\n'))
    if segundos == 0:
        print("El tiempo ha acabado!")


def main():
    registro()


main()
