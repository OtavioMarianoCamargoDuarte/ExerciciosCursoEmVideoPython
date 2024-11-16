from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        numero = randint(1, 10)
        lista.append(numero)
        print(f'{numero} ',end='',flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'Soma dos números pares: {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
