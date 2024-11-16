# Função que calcula e exibe a área do terreno
def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno com as dimensões: {largura}m x {comprimento}m = {area}m²')

# Programa Principal
print('=' * 26)
print(' CONTROLE DE TERRENOS '.center(26, '='))
print('=' * 26)
larg = float(input('Largura [m]: '))
compr = float(input('Comprimento [m]: '))
área(larg, compr)
