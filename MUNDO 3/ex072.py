por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    posicao = int(input('Digite um número entre 0 e 20: '))
    if posicao < 0 or posicao > 20:
        posicao = ('Número inválido! Digite novamente um número entre 0 e 20: ')
    else:
        print(f'{posicao} por extenso fica: {por_extenso[posicao]}')
        break
