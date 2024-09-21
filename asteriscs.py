# Diego Perea León A01708350
# asteriscos

YES = ['si', 'Si', 'SI','s']
NO = ['no', 'No', 'NO','n']


def sino(x2):
    while True:
        prog1 = input(x2)
        if prog1 in YES:
            return True
        elif prog1 in NO:
            return False
        else:
            print('No valido')


def dato(x):
    while True:
        try:
            w = int(input(x))
            if w > 0:
                return w
            else:
                print("Por favor, digite un numero entero positivo.")
        except ValueError:
            print("Por favor, digite un numero entero positivo.")


def process(x1, y1):
    for i in (1, y1 + 1):
        for j in (1, x1 + 1):
            print('x',end='')




def user():
    base = dato('Ingrese la base:\n')
    altura = dato('Ingrese la altura:\n')
    process(base, altura)
    prog = sino('Desea repetir el programa?(si/no)\n')
    return prog


def main():
    while True:
        loop = user()
        if not loop:
            break


main()
