# Diego Perea León a01703850
#  Ejercicio 1

def dato(x):
    while True:
        try:
            w = int(input(x))
            return w
        except ValueError:
            print("Por favor, ingrese un numero entero positivo")


def pares(a, b):
    if a < b:
        for i in range(a, b + 1):
            if i%2 == 0:
                print(i)
    else:
        print('Asegurese de que a < b')
        user()


def user():
    inicio = dato('Ingresa el valor con el que se va a iniciar:\n')
    limite = dato('Ingresa el valor a el que quieres llegar:\n')
    pares(inicio, limite)


user()
