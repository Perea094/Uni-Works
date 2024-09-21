# Diego Perea León
# T1_1_a01708350

print('Escribe 5 números')
letters = ['a', 'b', 'c', 'd', 'e']
numbers = []
for i in range(5):
    numbers.append(float(input(f'{letters[i]}: ')))

print(f'Número más grande: {max(numbers)}')
print(f'Número más pequeño: {min(numbers)}')
print(f'Promedio: {sum(numbers) / len(numbers)}')
