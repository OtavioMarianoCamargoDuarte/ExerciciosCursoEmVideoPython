lado_1 = float(input('Informe o 1º lado: '))
lado_2 = float(input('Informe o 2º lado: '))
lado_3 = float(input('Informe o 3º lado: '))


if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print('É possivel criarmos esse triângulo.')
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('Temos um triângulo EQUILÁTERO!')
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_3 != lado_2:
        print('Temos um triângulo ESCALENO!')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Temos um triângulo ISÓSCELES!')
else:
    print('Não podemos construir esse triângulo!')
