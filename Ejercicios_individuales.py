# Diego Perea León
# A01708350
# Dependiendo del score crediticio de un usuario, se da una tasa de interés para un crédito.


"""cred = float(input("Ingrese un score crediticio: "))
# El score va de 449 a 775 puntos
if cred >= 449 and cred <= 775:
    print("El credito es valido")
    if cred > 750:
        print("Tasa del 30% anual")
    elif cred <= 750 and cred >= 650:
        print("Tasa del 50% anual")
    elif cred < 650 and cred >= 500:
        print("Tasa del 65% anual")
    elif cred < 500:
        print("Tasa del 80% anual")
else:
    print("El credito no es valido")
    #
# Si el score es mayor a 750
# Tasa del 30% anual

# Si el score está entre 650 y 750
# Tasa del 50% anual

# Si el score está entre 500 y 649
# Tasa del 65% anual

# Si el score es menor de 500
# Tasa del 80% anual"""


def func1(sapo):
    func2 = False
    while not func2:
        try:
            sapo = float(sapo)
            func2 = True
            return sapo
        except ValueError:
            sapo = input('Ingrese un valor correcto: ')


print('Dame un valor:')
x = func1(input(""))
