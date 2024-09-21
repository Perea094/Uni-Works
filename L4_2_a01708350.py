# Diego Perea León A01708350
# Ejercicio 2

def areaRect(a, b):
    return a * b


def perimetroRect(a, b):
    return 2 * (a + b)


def main():
    largo = float(input("Largo: "))
    ancho = float(input("Ancho: "))
    p1 = input('¿Quiere calcular el área (a) o el perímetro (p) del rectángulo? \n')
    if p1 == 'a':
        print("Area: ", areaRect(largo, ancho))
    elif p1 == 'p':
        print("Perimetro: ", perimetroRect(largo, ancho))


main()
