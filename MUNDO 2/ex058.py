from random import randint
from time import sleep

numero = randint(0, 10)

print('\033[33m-=\033[m'*28)
print('\033[35mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[33m-=\033[m'*28)

palpite = ''
count = 1

while palpite != numero:
    palpite = int(input('Qual número pensei? '))
    print('\033[35mPROCESSANDO...\033[m')
    sleep(1)
    if palpite != numero and 0 <= palpite <= 10:
        if palpite < numero:
            print('ERROU! TENTE NOVAMENTE. O NÚMERO É MAIOR')
            count += 1
        else:
            print('ERROU! TENTE NOVAMENTE. O NÚMERO É MENOR')
            count += 1
    elif palpite < 0 or palpite > 10:
        print('O número está entre 0 e 10!')
    else:
        print('VOCÊ ACERTOU NA {}ª TENTATIVA, PENSEI NO NÚMERO {}!'.format(
            count, numero))
