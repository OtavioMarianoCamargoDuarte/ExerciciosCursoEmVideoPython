from random import randint
from time import sleep
from operator import itemgetter

numeros_sorteados = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}

ranking = list()

'''OUTRA FORMA DE ORGANIZAR DICIONÁRIO DE FORMA DECRESCENTE
ranking = dict(sorted(numeros_sorteados.items(), key=lambda item: item[1], reverse=True))'''


print('<<<< Valores sorteados >>>>')
for k, i in numeros_sorteados.items():
    print(f'O {k} tirou {i}')
    sleep(1)

ranking = sorted(numeros_sorteados.items(), key=itemgetter(1), reverse=True)

print('<<<< Ranking dos jogadores >>>> ')
for k, i in enumerate(ranking):
    print(f'{k+1}ºLugar: {i[0]} com {i[1]}')
    sleep(1)
