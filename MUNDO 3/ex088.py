from random import randint
from time import sleep

print('=' * 36)
print(' MEGA DA VIRADA '.center(36, '='))
print('=' * 36)

sorteio = []

quantidade_sorteios = int(input('Digite quantos jogos você deseja: '))

print('=' * 36)

for s in range(quantidade_sorteios):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    sorteio.append(jogo)

for e in range(0, len(sorteio)):
    print(f'Jogo {e + 1:2}: {sorteio[e]}')
    sleep(1)
print('=' * 36)
