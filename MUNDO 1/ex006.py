from math import sqrt

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)

print('O número escolhido foi: {}'.format(num))
print('{} x 2 = {}'.format(num, dobro))
print('{} x 3 = {}'.format(num, triplo))
print('A raiz de {} = {:.2f}'.format(num, raiz))
