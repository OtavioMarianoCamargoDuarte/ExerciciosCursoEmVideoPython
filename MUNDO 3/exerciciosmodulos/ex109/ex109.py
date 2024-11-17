import moeda_109

preco = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda_109.moeda(preco)} é: {moeda_109.metade(preco, True)}')
print(f'O dobro de {moeda_109.moeda(preco)} é: {moeda_109.dobro(preco, True)}')
taxa_aumento = float(input('Informe a taxa de aumento (%): '))
print(f'Valor Inicial: {moeda_109.moeda(preco)} com {taxa_aumento}% de aumento ficou: {moeda_109.aumentar(preco, taxa_aumento, True)}')
taxa_desconto = float(input(f'Informe ataxa de desconto (%): '))
print(f'Valor Inicial: {moeda_109.moeda(preco)} com {taxa_desconto}% de desconto ficou: {moeda_109.diminuir(preco, taxa_desconto, True)}')
