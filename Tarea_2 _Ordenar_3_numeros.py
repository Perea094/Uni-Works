# Diego Perea León A01708350
# Tarea 2 - Ordenar 3 números
# Hacer un programa que pida 3 numeros de punto flotante
# al usuario, los ordene de menor a mayor
# y los muestre en pantalla

a, b, c = float(input("Digite un valor: ")), float(input("Digite un valor: ")), float(input("Digite un valor: "))

if a > b:
    x = a
    a = b
    b = x
    if b > c:
        x = c
        c = b
        b = x
    if a > b:
        x = a
        a = b
        b = x
if b > c:
    x = c
    c = b
    b = x
    if a > b:
        x = a
        a = b
        b = x
print(f'\n{a}\n{b}\n{c}')
