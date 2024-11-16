from random import randint

vitoria_jogador = vitoria_computador = 0

while True:
    computador = randint(0, 10)
    par_ou_impar = input('Par ou Ímpar: ').upper().strip()[0]
    jogador = int(input('Coloque o número: '))
    soma = computador + jogador

    if (par_ou_impar == 'P' and soma % 2 == 0) or (par_ou_impar == 'I' and soma % 2 != 0):
        vitoria_jogador += 1
        print(f'Jogador {vitoria_jogador} x {vitoria_computador} Computador')
        print('='*25)
    else:
        vitoria_computador += 1
        if vitoria_computador == 1:
            print(f'Você perdeu! Porém conseguiu {vitoria_jogador} vitorias')
            break
