soma_idades = 0
h_velho = 0
mulheres_menores = 0
nome_h_velho = ''

for c in range(0, 4):
    nome = input('NOME: ').upper()
    idade = int(input('IDADE: '))
    sexo = input('SEXO: ')
    if sexo == 'masculino' and idade > h_velho:
        h_velho = idade
        nome_h_velho = nome
    if sexo == 'feminino' and idade < 20:
        mulheres_menores += 1
    print('='*15)
    soma_idades += idade

media_idades = soma_idades / (c + 1)

print('MA MÉDIA DAS IDADES É: {}'.format(media_idades))
print('O HOMEM MAIS VELHO É: {}'.format(nome_h_velho))
print('{} MULHERES TEM MENOS DE 20 ANOS.'.format(mulheres_menores))
