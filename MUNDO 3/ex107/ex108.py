import moeda


preco = float(input('Digite um preço: R$'))
print(f'A metade de R${moeda.moeda(preco)} é: R${
      moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de R${moeda.moeda(preco)} é R${
      moeda.moeda(moeda.metade(preco))}')
taxa_aumento = float(input('Informe a taxa de aumento (%): '))
print(f'Valor Inicial: R${moeda.moeda(preco)} com {taxa_aumento}% de aumento ficou R${
      moeda.moeda(moeda.aumentar(preco, taxa_aumento))}')
taxa_desconto = float(input('Informe a taxa de desconto (%): '))
print(f'Valor Inicial: R${moeda.moeda(preco)} com {taxa_desconto}% de desconto ficou R${
      moeda.moeda(moeda.diminuir(preco, taxa_desconto))}')
