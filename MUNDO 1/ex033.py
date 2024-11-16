num_1 = int(input('Informe o 1º número: '))
num_2 = int(input('Informe o 2º número: '))
num_3 = int(input('Informe o 3º número: '))

maior = 0
menor = 0

if num_1 > num_2 and num_1 > num_3:
    maior = num_1
    if num_2 < num_3:
        menor = num_2
    else:
        menor = num_3
    print('{} é o maior.\n{} é o menor'.format(maior, menor))

if num_2 > num_1 and num_2 > num_3:
    maior = num_2
    if num_1 < num_3:
        menor = num_1
    else:
        menor = num_3
    print('{} é o maior.\n{} é o menor.'.format(maior, menor))

if num_3 > num_1 and num_3 > num_2:
    maior = num_3
    if num_1 < num_2:
        menor = num_1
    else:
        menor = num_2
    print('{} é o maior.\n{} é o menor.'.format(maior, menor))
