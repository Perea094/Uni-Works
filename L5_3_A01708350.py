# Diego Perea León A01708350
# L5_3_A01708350
# Ejercicio 3

def func1(x):
    while True:
        try:
            w = float(input(x))
            return w
        except ValueError:
            print("Introduzca un valor ")


def func2(i1, i2):
    i4 = i1*(1 + i2)
    c = 1
    print(f'{c}, {i4:.02f}')
    while not (i4 > (2 * i1)):
        i4 = i4*(1 + i2)
        c += 1
        print(f'{c}, {i4:.02f}')


def main():
    mi = func1('Monto a invertir = \t')
    tia = func1('Tasa de interes anual = \t')
    func2(mi, tia)


main()
