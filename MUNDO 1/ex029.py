velocidade = int(input('Informe a velocidade do carro (em km/h): '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você passou no radar a {}km/h, deverá pagar uma multa de R${:.2f}'.format(velocidade, multa))
else:
    print('Siga viagem!')
