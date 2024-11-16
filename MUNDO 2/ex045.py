from random import choice
from time import sleep

# ESCOLHA DO COMPUTADOR
lista_computador = ['pedra', 'papel', 'tesoura']
computador = choice(lista_computador)

print(' \033[1;34;44mJOKENPYTHON!\033[m '.center(60, '='))
print(' \033[1;34;44mFAÇA SUA ESCOLHA\033[m '.center(60, '='))
print('\033[1;32;44m// PEDRA // PAPEL // TESOURA //\033[m'.center(60))
print('='*47)
jogador = input('Escolha: ').lower()
print('='*47)

if jogador == computador:
    sleep(2)
    print('...JO...'.center(20))
    sleep(2)
    print('...KEN...'.center(30))
    sleep(2)
    print('...PYTHON...'.center(40))
    sleep(2)
    print('\033[33mEMPATOU!\033[m'.center(55))
    print('Os dois jogadores escolheram {}'.center(
        42).format(computador).upper())
    print('='*47)
elif (computador == 'pedra' and jogador == 'tesoura') or (computador == 'papel' and jogador == 'pedra') or (computador == 'tesoura' and jogador == 'papel'):
    sleep(2)
    print('...JO...'.center(20))
    sleep(2)
    print('...KEN...'.center(30))
    sleep(2)
    print('...PYTHON...'.center(40))
    sleep(2)
    print('\033[31mPERDEU!\033[m'.center(55))
    print('COMPUTADOR: {} x {} :JOGADOR'.center(
        40).format(computador, jogador).upper())
    print('='*47)
else:
    sleep(2)
    print('...JO...'.center(20))
    sleep(2)
    print('...KEN...'.center(30))
    sleep(2)
    print('...PYTHON...'.center(40))
    sleep(2)
    print('\033[32mVENCEU!\033[m'.center(55))
    print('COMPUTADOR: {} x {} :JOGADOR'.center(
        40).format(computador, jogador).upper())
    print('='*47)
