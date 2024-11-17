import moeda_108

preco = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda_108.moeda(preco)} é: {
      moeda_108.moeda(moeda_108.metade(preco))}')
print(f'O dobro de {moeda_108.moeda(preco)} é: {
      moeda_108.moeda(moeda_108.dobro(preco))}')
taxa_aumento = float(input('Informe a taxa de aumento (%): '))
print(f'Valor Inicial: {moeda_108.moeda(preco)} com {taxa_aumento}% de aumento ficou: {
      moeda_108.moeda(moeda_108.aumentar(preco, taxa_aumento))}')
taxa_desconto = float(input(f'Informe ataxa de desconto (%): '))
print(f'Valor Inicial: {moeda_108.moeda(preco)} com {taxa_desconto}% de desconto ficou: {
      moeda_108.moeda(moeda_108.diminuir(preco, taxa_desconto))}')
