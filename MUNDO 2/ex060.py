n = int(input('Informe um número e veja seu fatorial: '))
c = n
f = 1

print('{}! = '.format(n), end='')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
