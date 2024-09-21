# Diego Perea León A01708350

# Aprox pi
# For



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


def aproxPi(iteraciones):
    sumatoria = 0
    for denominador in range(2,(iteraciones*2)+1,2):
        sumatoria += 1 / (denominador**2)
    return sumatoria


def div(x1):
    x = aproxPi(x1)
    calc = (24 * x) ** (1 / 2)
    return calc


def user():
    print("Welcome to Python Program")
    w1 = dato('Ingrese la cantidad de iteraciones\n')
    w2 = div(w1)
    print("La cantidad de iteraciones es: ", w2)

user()