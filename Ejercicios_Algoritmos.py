# Diego Perea León
# A01708350
# 19/09/2024
# Ejercicios: Algoritmos


# Ejercicio 1
# Escribe un algoritmo para verificar si un precio dado por el usuario es válido o
# no lo es, para ser válido debe ser un valor positivo.
def dato_flotante(x):
    while True:
        try:
            w = float(input(x))
            return w
        except ValueError:
            print('Error Ingrese un número...')


def ejercicio1():
    precio = dato_flotante('Ingrese el precio del producto:\n')
    if precio > 0:
        print('Valido')
    else:
        print('No valido')


# Ejercicio 2
# Escribe un algoritmo que muestre la velocidad promedio de un automóvil dadas
# la distancia recorrida en kilómetros y el tiempo que se tardó en recorrer esa distancia dado en horas.

def dato_flotante_positivo(x1):
    while True:
        try:
            w1 = float(input(x1))
            if w1 > 0:
                return w1
            else:
                print('Error Ingrese un número positivo...')
        except ValueError:
            print('Error Ingrese un número positivo...')


def ejercicio2():
    distancia_km = dato_flotante_positivo('Ingrese la distancia en km:\n')
    tiempo_horas = dato_flotante_positivo('Ingrese el tiempo que se tardó en recorrer esa distancia en horas:\n')
    print(f'La velocidad promedio del automóvil es {distancia_km / tiempo_horas:.2f} km / h')


# Ejercicio 3
# Escribe un algoritmo que dada una longitud en metros, calcule y muestre su equivalente en pies.
# Recuerda que 1 pie = 12 pulgadas, 1 pulgada = 2.54 cm, 1 m = 100 cm

def ejercicio3():
    longitud_metros = dato_flotante_positivo('Ingrese la longitud de metros que desea convertir:\n')
    longitud_centimetros = longitud_metros * 100
    longitud_pulgadas = longitud_centimetros / 2.54
    longitud_pies = longitud_pulgadas / 12
    print(f'{longitud_metros} m es igual a:'
          f'\n- {longitud_centimetros:.2f} cm\n'
          f'- {longitud_pulgadas:.2f} inch\n'
          f'- {longitud_pies:.2f} ft')


# Ejercicio 4
# Escribe un algoritmo que verifique si una persona puede obtener su licencia de conducir.
# Para hacerlo debe ser mayor de edad (18 años o más) y traer una identificación oficial.

YES = ['yes', 'si', 's', 'y']
NO = ['no', 'n']


def dato_entero_positivo(x2):
    while True:
        try:
            w2 = int(input(x2))
            if w2 > 0:
                return w2
            else:
                print('Error Ingrese un número entero positivo')
        except ValueError:
            print('Error No valido')


def dato_Yes_No(x3):
    while True:
        w3 = input(x3)
        if w3.lower() in YES or w3.lower() in NO:
            return w3
        else:
            print('Error')


def ejercicio4():
    edad = dato_entero_positivo('Ingrese la edad:\n')

    if edad >= 18:
        identificacion = dato_Yes_No('Trae una identificación oficial:\n')
        if identificacion.lower() in YES:
            print(f'Puede tener licencia de conducir')
        else:
            print(f'No cumple con alguno de los requisitos.')
    else:
        print(f'No cumple con alguno de los requisitos.')


def menu():
    while True:
        print(f'\nQué desea hacer?\n'
              f'1. Ejercicio 1 (Verificador de precio)\n'
              f'2. Ejercicio 2 (Velocidad promedio)\n'
              f'3. Ejercicio 3 (Transformador de longitudes)\n'
              f'4. Ejercicio 4 (Verificador de licencia de conducir)\n'
              f'5. Salir\n')
        desicion = dato_entero_positivo('')
        if 5 >= desicion >= 1:
            return desicion
        else:
            print('Error')


def main():
    while True:
        user_choice = menu()
        if user_choice == 1:
            ejercicio1()
        elif user_choice == 2:
            ejercicio2()
        elif user_choice == 3:
            ejercicio3()
        elif user_choice == 4:
            ejercicio4()
        elif user_choice == 5:
            break


main()
