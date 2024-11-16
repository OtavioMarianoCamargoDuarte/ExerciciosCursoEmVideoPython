print('=' * 21)
print(' GERADOR DE PA '.center(21, '='))
print('=' * 21)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
print('=' * 21)

termo = primeiro
count = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1

    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

