largura = float(input('Informe a largura (em m): '))
altura = float(input('Informe a altura (em m): '))
area = largura * altura
litro = area / 2

print('A área da parede é de {:.1f}m², para pintá-la precisariamos de {:.1f}L de tinta.'.format(area, litro))
