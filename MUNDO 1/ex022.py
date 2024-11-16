nome = str(input('Informe seu nome completo: '))

# Retirando todos espaços do ínicio e fim
sespaco = nome.strip()
# Retirando os espaços do meio
ncarac = len(sespaco.replace(' ', ''))
# "splitando" a frase (coloando em lista)
separar = sespaco.split()

print('O nome {} com todas as letras maiúsculas ficaria {}'.format(
    sespaco, sespaco.upper()))

print('O nome {} com todas as letras minúsculas ficaria {}'.format(
    sespaco, sespaco.lower()))

print('No nome {}, possuem {} letras.'.format(sespaco, ncarac))

print('No primeiro nome que é {} possuem {} letras.'.format(
    separar[0], len(separar[0])))
