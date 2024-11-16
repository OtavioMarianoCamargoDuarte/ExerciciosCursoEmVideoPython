numero = int(input('Informe um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10


print('UNIDADE: {}'.format(unidade))
print('DEZENA: {}'.format(dezena))
print('CENTENA: {}'.format(centena))
print('MILHAR: {}'.format(milhar))
