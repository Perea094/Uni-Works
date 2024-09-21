# Diego Perea León a01708350
# progama que calcula el crecimiento de interés compuesto

def calc_int(monto, tasa):
    monto = monto * (1 + tasa)
    return monto


def main():
    # codigo
    inversion_inicial = float(input("Ingrese el valor inicial: $\t"))
    tasa = float(input("Ingrese la tasa aunal:\t"))
    valor = inversion_inicial
    year = 0

    while valor < 2 * inversion_inicial:
        year += 1
        valor = calc_int(valor, tasa)
        print(valor)


main()
