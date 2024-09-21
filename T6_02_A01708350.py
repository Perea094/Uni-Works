# Diego Perea León A01708350
# Ejercio 2

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


def sumatoria(n):
    sumatoria1 = 0
    for i in range(1, n + 1):
        sumatoria1 += (3 ** i) / i
    return sumatoria1


def main():
    cantidad = dato('Ingrese un número entero para imprime en pantalla el resultado de la sumatoria\n')
    print(f"El resultado de la sumatoria es {sumatoria(cantidad)}")


main()
