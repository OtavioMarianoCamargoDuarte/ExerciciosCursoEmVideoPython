from ex107 import moeda


preco = float(input('Digite um preço: R$'))
print(f'A metade de R${preco:.2f} é: R${moeda.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}')
taxa_aumento = float(input('Informe a taxa de aumento (%): '))
print(f'Valor Inicial: R${preco:.2f} com {taxa_aumento}% de aumento ficou R${moeda.aumentar(preco, taxa_aumento):.2f}')
taxa_desconto = float(input('Informe a taxa de desconto (%): '))
print(f'Valor Inicial: R${preco:.2f} com {taxa_desconto}% de desconto ficou R${moeda.diminuir(preco, taxa_desconto):.2f}')
