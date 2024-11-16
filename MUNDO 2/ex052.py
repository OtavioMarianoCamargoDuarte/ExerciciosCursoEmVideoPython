numero = int(input('Informe um número inteiro: '))
cont = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        cont += 1
if cont == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')
