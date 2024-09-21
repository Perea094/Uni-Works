# Diego Perea León A01708350
# Laboratorio 9
import random


def datoint(x):
    while True:
        try:
            w = int(input(x))
            return w
        except ValueError:
            print('Ingrese un numero entero...')


def datointpositivo(x1):
    while True:
        try:
            w1 = int(input(x1))
            if w1 > 0:
                return w1
            else:
                print('Ingrese un número entero positivo...')
        except ValueError:
            print('Ingrese un numero entero...')


def creaLista(size):
    A1 = []
    for i in range(size):
        A1.append(random.randint(-50, 50))
    return A1


def imprimeLista(A):
    for i1 in range(len(A)):
        print(f'lista [{i1}] = {A[i1]}')


def cuentaNegativos(A):
    cantN = 0
    for i in range(len(A)):
        if A[i] < 0:
            cantN += 1
    print(f"El resultado de la función es: {cantN}")


def promedio(A):
    print(f"El resultado de la función es: {sum(A) / len(A)}")


def sustituyeLista(A, x, y):
    for i in range(len(A)):
        if A[i] == x:
            A[i] = y


def mueveLista(A):
    A.reverse()
    print(A)


def menu():
    print('\n1.\tImprime lista\n2.\tCuenta Negativos\n'
          '3.\tPromedio lista\n4.\tSustituye lista\n5.\tMueve lista\n'
          '6.\tSalir del programa')


def main():
    t = datointpositivo('Introduce el tamaño de la lista:\t')
    A = creaLista(t)
    while True:
        menu()
        opcion = datoint('')
        if opcion == 1:
            imprimeLista(A)
        elif opcion == 2:
            cuentaNegativos(A)
        elif opcion == 3:
            promedio(A)
        elif opcion == 4:
            numRemplazo = datoint('Ingresa el numero que se va a reemplazar:\t')
            Remplazo = datoint('Ingresa el reemplazo:\t')
            sustituyeLista(A, numRemplazo, Remplazo)
        elif opcion == 5:
            mueveLista(A)
        elif opcion == 6:
            print('Adios...')
            break
        else:
            print('ERROR\tOpción invalida')


main()
