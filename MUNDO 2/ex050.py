soma_pares = 0
cont = 0

for c in range(0, 6):
    numero = int(input(('Insira um número: ')))
    if numero % 2 == 0:
        soma_pares += numero
        cont += 1
print('A soma dos {} números pares digitados foi: {}'.format(cont, soma_pares))
