notas_50 = notas_20 = notas_10 = notas_1 = 0

valor = int(input('Valor a ser sacado: R$'))

notas_50 = valor // 50
valor %= 50

notas_20 = valor // 20
valor %= 20

notas_10 = valor // 10
valor %= 10

notas_1 = valor // 1
valor %= 1

print(f'{notas_50} Cédulas de R$50,00\n{notas_20} Cédulas de R$20,00\n{notas_10} Cédulas de R$10,00\n{notas_1} Cédulas de R$1,00')
