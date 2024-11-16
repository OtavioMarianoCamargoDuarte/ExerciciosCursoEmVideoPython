s = 0
qtd = 0

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        qtd += 1

print('A soma de todos os {} números ímpares entre 1 e 500 é: {}'.format(qtd, s))
