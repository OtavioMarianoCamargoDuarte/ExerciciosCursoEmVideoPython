from time import sleep

print('=' * 22)
valor_1 = int(input('Informe um valor: '))
valor_2 = int(input('Informe um valor: '))
opcao = 0

while opcao != 5:
    print(' MENU '.center(22, '='))
    print('[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR DO PROGRAMA')
    opcao = int(input('Opção: '))
    print('=' * 22)
    if opcao == 1:
        soma = valor_1 + valor_2
        print('{} + {} = {}'.format(valor_1, valor_2, soma))
    elif opcao == 2:
        multiplicacao = valor_1 * valor_2
        print('{} x {} = {}'.format(valor_1, valor_2, multiplicacao))
    elif opcao == 3:
        if valor_1 > valor_2:
            maior = valor_1
        else:
            maior = valor_2
        print('Maior: {}'.format(maior))
    elif opcao == 4:
        valor_1 = int(input('Informe um valor: '))
        valor_2 = int(input('Informe um valor: '))
    elif opcao == 5:
        break
    else:
        print('Opção Inválida!')

print('Finalizando Programa'.center(22))
sleep(2)
print('FIM DO PROGRAMA'.center(22))
