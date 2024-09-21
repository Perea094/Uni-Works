# Diego Perea León A01708350
# Calculadora
# Tarea 2: Funciones con Decisiones
import math
def operacion(a, b, c):
    if a == 's':
        d = b + c
        return d
    elif a == 'r':
        d = b - c
        return d
    elif a == 'm':
        d = b * c
        return d
    elif a == 'd':
        d = b / c
        return d
    elif a == 'R':
        d = math.pow(b, 1/c)
        return d

def main():
    x = input('Qué operación aritmética desea hacer: \n(s)\tSuma \n(r)\tResta \n(m)\tMultiplicación \n(d)\tDivisión \n(R)\tRaíz\n')
    x1 = float(input('Ingrese el primer valor: '))
    x2 = float(input('Ingrese el segundo valor: '))
    print(f'El resultado de su operación es :\n{operacion(x, x1, x2)}')

main()
