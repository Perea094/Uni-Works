# Diego Perea León A01708350
# Ejercicio 3

def dato(x):
    while True:
        try:
            w = int(input(x))
            if w >= 0:
                return w
            else:
                print("Por favor, ingrese un numero entero positivo")
        except ValueError:
            print("Por favor, ingrese un numero entero positivo")


def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


def main():
    user = dato('Ingrese el numero que desea calcular\n')
    print(factorial(user))


main()
