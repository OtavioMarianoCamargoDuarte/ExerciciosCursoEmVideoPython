print('-='*20)
print("ANALISANDO TRIÂNGULOS".center(40))
print('-='*20)
lado_1 = float(input('Informe o 1º lado do triângulo: '))
lado_2 = float(input('Informe o 2º lado do triângulo: '))
lado_3 = float(input('Informe o 3º lado do triângulo: '))

if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2:
    print('Podemos criar um triângulo com os lados {} , {} , {}.'.format(
        lado_1, lado_2, lado_3))
else:
    print('Triângulo impossivel de ser criado.')
