frase = str(input('Escreva uma frase: ').strip().replace(' ', '').upper())
frase_inv = frase[::-1]

if frase == frase_inv:
    print('A frase: {} \033[32mÉ UM PALÍNDROMO!\033[m\nFrase Escrita: {}\nFrase Invertida: {}'.format(frase, frase, frase_inv))
else:
    print('A frase: {} \033[31mNÃO É UM PALÍNDROMO!\033[m\nFrase Escrita: {}\nFrase Invertida {}'.format(frase, frase, frase_inv))