# Diego Perea León A01708350
# Ejercicio 1
# print('Hola mundo')

def num(x):
    while True:
        try:
            w = float(input(x))
            return w
        except ValueError:
            print('Ingrese un número.')


def looP(t, q):
    while t <= q:
        if t % 2 == 0:
            print(t)
        t += 1


def main():
    a, b = 0, 0
    print('a < b')
    while not (a < b):
        a = num('Dame el número a:\t')
        b = num('Dame el número b.\t')
    looP(a, b)


main()
