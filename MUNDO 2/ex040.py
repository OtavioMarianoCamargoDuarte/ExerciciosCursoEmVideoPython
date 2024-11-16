nota_1 = float(input('Informe a 1ª nota: '))
nota_2 = float(input('Informe a 2ª nota: '))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print('PARABENS! VOCÊ FOI APROVADO!')
elif 5 <= media <= 6.9:
    print('CUIDADO! VOCÊ ESTÁ DE RECUPERAÇÃO!')
elif media < 5:
    print('ESTUDE MAIS! VOCÊ FOI REPROVADO!')