# Diego Perea León A01708350
# Tarea 3


def dato(x):
    while True:
        try:
            w = int(input(x))
            if w >= -1:
                return w
            else:
                print("Por favor, ingrese un numero dentro del rango disponible")
        except ValueError:
            print("Por favor, ingrese un numero entero positivo")


def desarrollo():
    usuario = dato('Dame un número positivo, (-1 para salir):\t')
    cantidad = 0
    suma = 0
    while usuario >= 0:
        cantidad += 1
        suma += usuario
        usuario = dato('Dame un número positivo, (-1 para salir):\t')

    print(f'Números ingresados:\t{cantidad}')

    if cantidad == 0:
        try:
            suma/cantidad
        except ZeroDivisionError:
            print("Se termino el programa")
    else:
        print(f'Suma total:\t{suma}')
        print(f'Promedio:\t{suma / cantidad :.2f}')


desarrollo()
