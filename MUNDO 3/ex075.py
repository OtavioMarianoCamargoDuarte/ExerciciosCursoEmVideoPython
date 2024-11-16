numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os números: {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if numeros.count(3) == 0:
    print('O número 3 não foi digitado em nenhuma posição.')
else:
    print(f'O número 3 foi digitado na posição {numeros.index(3) + 1}')

print(f'Os números pares digitados foram:', end=' ')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
print()