print('=' * 21)
print(' GERADOR DE PA '.center(21, '='))
print('=' * 21)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
print('=' * 21)

termo = primeiro
count = 1

while count <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    count += 1

print('FIM')
