numero = int(input('Informe um número: '))
base_conv = int(
    input('1 - Binário\n2 - Octal\n3 - Hexadecimal\nInforme a Base de Conversão: '))

if base_conv == 1:
    binario = bin(numero)[2:]
    print('Inteiro: {} >>> Binário: {}'.format(numero, binario))
elif base_conv == 2:
    octal = oct(numero)[2:]
    print('Inteiro: {} >>> Octal: {}'.format(numero, octal))
elif base_conv == 3:
    hexa = hex(numero)[2:]
    print('Inteiro: {} >>> Hexadecimal: {}'.format(numero, hexa))
else:
    print('Valor Inválido')
