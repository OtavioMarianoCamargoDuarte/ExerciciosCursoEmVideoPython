from datetime import date

maiores = 0
menores = 0

ano_atual = date.today().year

for c in range(0, 7):
    ano_nasc = int(input('Informe seu ano de nascimento: '))
    maioridade = ano_atual - ano_nasc
    if maioridade >= 18:
        maiores += 1
    else:
        menores += menores + 1

print('{} Pessoas +18'.format(maiores))
print('{} Pessoas -18'.format(menores))
