num_1 = int(input('Informe o 1º valor: '))
num_2 = int(input('Informe o 2º valor: '))


if num_1 > num_2:
    print('O 1º valor digitado foi {} e ele é o maior.'.format(num_1))
elif num_2 > num_1:
    print('O 2º valor digitado foi {} e ele é o maior'.format(num_2))
else:
    print('Os dois números digitados são iguais.')
