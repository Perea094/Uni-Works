# Diego Perea León A01708350
# Ejercicio 1
# Convertidor °C <-> °F

def dato(x):
    while True:
        try:
            w = float(input(x))
            return w
        except ValueError:
            print('Ingrese un valor en decimal.')


def unodos(x1):
    while True:
        w1 = dato(x1)
        if w1 in [1, 2, 3]:
            return w1
        else:
            print('Ingrese un valor valido.')


def CtoF(C):
    return (C * 9 / 5) + 32


def FtoC(F):
    return (F - 32) * 5 / 9


def seleccion():
    print(
        'Bienvenido al convertidor de unidades de temperatura...\n¿Qué deseas convertir?\n1.\tCentígrados a '
        'Fahrenheit\n2.\tFahrenheit a Centígrados\n3.\tSalir')
    seleccion1 = unodos('')
    return seleccion1


def intro():
    seleccion2 = seleccion()
    if seleccion2 == 1:
        valor = dato('Dame la temperatura en °C:\t')
        valor2 = CtoF(valor)
        print(f'\n{valor} °C = {valor2:.2f} °F\n')
    elif seleccion2 == 2:
        valor = dato('Dame la temperatura en °F:\t')
        valor2 = FtoC(valor)
        print(f'\n{valor} °F = {valor2:.2f} °C\n')
    elif seleccion2 == 3:
        return False


def main():
    while True:
        loop = intro()
        if not loop:
            break


main()
