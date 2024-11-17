from moeda_107 import metade, dobro, aumentar, diminuir

preco = float(input('Digite um preço: R$ '))
print(f'A metade de R${preco} é: R${metade(preco)}')
print(f'O dobro de R${preco} é R${dobro(preco)}')
taxa_aumento = float(input('Informe a taxa de aumento (%): '))
print(f'Valor Inicial: R${preco} com {taxa_aumento}% de aumento ficou R${aumentar(preco, taxa_aumento)}')
taxa_desconto = float(input('Informe a taxa de desconto (%): '))
print(f'Valor Inicial: R${preco} com {taxa_desconto}% de desconto ficou R${diminuir(preco, taxa_desconto)}')

