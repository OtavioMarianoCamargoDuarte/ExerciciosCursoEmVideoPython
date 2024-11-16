import math

primeiro_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termos = int(input('Informe quantos termos quer ver: '))

for c in range(primeiro_termo, primeiro_termo + (razao * termos), razao):
    print(c, end=' -> ')
print('FIM')
