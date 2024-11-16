numero = int(input('Insira o número que deseja ver a tabuada: '))
quantidade = int(input('Insira o valor limite da tabuada: '))

for c in range(0, quantidade + 1):
    print('{} x {:2} = {}'.format(numero, c, numero * c))
