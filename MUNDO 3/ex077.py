palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

vogais = ('A', 'E', 'I', 'O', 'U')

for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra in vogais:
            print(letra, end=' ')
print()

'''for palavra in palavras:
    vogais_encontradas = set()
    for letra in palavra:
        if letra in vogais:
            vogais_encontradas.add(letra)

    if vogais_encontradas:
        print(f'Na palavra {palavra}, temos as vogais: {
              ','.join(vogais_encontradas)}')
    else:
        print(f'Na palavra {palavra}, não há vogais')
'''
