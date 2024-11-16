from datetime import date

ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade <= 9:
    print('O atleta pertence a categoria: MIRIM\nPois tem {} anos.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta pertence a categoria: INFANTIL\nPois tem {} anos.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta pertence a categoria: JUNIOR\nPois tem {} anos.'.format(idade))
elif 19 < idade <= 20:
    print('O atleta pertence a categoria: SÊNIOR\nPois tem {} anos.'.format(idade))
else:
    print('O atleta pertence a categoria: MASTER\nPois tem {} anos.'.format(idade))
