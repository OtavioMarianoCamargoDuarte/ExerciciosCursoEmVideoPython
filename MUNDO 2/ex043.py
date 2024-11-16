peso = float(input('Informe o Peso (em kg): '))
altura = float(input('Informe a altura (em m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('VOCÊ ESTÁ COM IMC {:.2f}KG/M² E ESTÁ ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25:
    print('VOCÊ ESTÁ COM IMC {:.2f}KG/M² E ESTÁ NO PESO IDEAL.'.format(imc))
elif 25 <= imc <= 30:
    print('VOCÊ ESTÁ COM IMC {:.2f}KG/M² E ESTÁ COM SOBREPESO.'.format(imc))
elif 30 < imc <= 40:
    print('VOCÊ ESTÁ COM IMC {:.2f}KG/M² E ESTÁ COM OBESIDADE.'.format(imc))
elif imc > 40:
    print(
        'VOCÊ ESTÁ COM IMC {:.2f}KG/M² E ESTÁ COM OBESIDADE MÓRBIDA.'.format(imc))
