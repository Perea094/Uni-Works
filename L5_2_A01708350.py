# Diego Perea León A01708350
# L5_2_A01708350
# Ejercicio 2

def func3(m1):
    while True:
        try:
            m = float(input(m1))
            return m
        except ValueError:
            print("Por favor, ingrese un número.")


def func4(m2, m3):
    while m2 < 1000:
        m4 = m2 + m3
        return m4


def func2():
    print('Ingrese numero(s)')
    z = 0
    cn = 0
    while z < 1000:
        a = func3('')
        z = func4(z, a)
        cn += 1
    print(f'Suma= {z}\nCantidad de números= {cn}')


func2()
