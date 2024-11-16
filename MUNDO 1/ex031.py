distancia = int(input('Informe a distância da viagem (em km): '))
valor_Km = 0

if distancia <= 200:
    valor_Km = 0.5
    valor_total = distancia * valor_Km
    print('{}km x R${:.2f}/km\nValor Total: R${:.2f}'.format(distancia,
          valor_Km, valor_total))
else:
    valor_Km = 0.45
    valor_total = distancia * valor_Km
    print('{}km x R${:.2f}/km\nValor Total: R${:.2f}'.format(distancia,
          valor_Km, valor_total))


