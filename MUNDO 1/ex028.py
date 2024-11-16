from random import randint
from time import sleep

numero = randint(0, 5)
print('\033[33m-=\033[m'*28)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=\033[m'*28)

palpite = int(input('Qual número pensei? '))

print('\033[35mPROCESSANDO...\033[m')
sleep(2)

if palpite == numero:
    print('\033[32mParabéns! Meu número foi realmente o {}.\033[m'.format(numero))
else:
    print('\033[31mQue pena, eu pensei no número {}.\033[m'.format(numero))
