dados_jogador = {}
gols = []

dados_jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
quantidade_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou ? '))


for c in range(quantidade_partidas):
    gols_partida = int(input(f'Quantos gols na partida {c}: '))
    gols.append(gols_partida)

dados_jogador['gols'] = gols
dados_jogador['total'] = sum(gols)

print('=' * 25)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 25)

print(f'O jogador {dados_jogador["nome"]} jogou {quantidade_partidas} partidas.')

for k, v in enumerate(gols):
    print(f'  => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {dados_jogador["total"]} gols.')
