from random import randint

sorteados = (randint(0, 9), randint(0, 9), randint(
    0, 9), randint(0, 9), randint(0, 9))

sorteados_em_ordem = (sorted(sorteados))

print(f'Os números sorteados foram {sorteados[0]} {
      sorteados[1]} {sorteados[2]} {sorteados[3]} {sorteados[4]}')
print(f'O maior valor sorteado foi: {sorteados_em_ordem[0]}')
print(f'O menor valor sorteado foi: {sorteados_em_ordem[4]}')
