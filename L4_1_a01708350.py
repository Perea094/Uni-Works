# Diego Perea León A01708350
# Ejercicio 1


def func1(q):
    q1 = False
    while not q1:
        try:
            q = float(q)

            return q
        except ValueError:
            q = input("Please enter a number: ")


def equivalente(a, b, c):
    a *= 3600
    b *= 60
    d = a + b + c
    return d


def main():
    h = (func1(input("Horas: ")))
    m = (func1(input("Minutos: ")))
    s = (func1(input("Segundos: ")))
    f = equivalente(h, m, s)
    print(f'{f} segundos')


main()
