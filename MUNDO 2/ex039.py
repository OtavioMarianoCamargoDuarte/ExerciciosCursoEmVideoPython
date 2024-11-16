from datetime import date

ano_nasc = int(input('Informe o ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    print('Você ainda tem que esperar {} anos para se alistar.'.format(18 - idade))
elif idade == 18:
    print('ATENÇÃO! Você deve se alistar esse ano!')
else:
    print('Já se passaram {} anos que você deveria ter se alistado.'.format(idade - 18))
