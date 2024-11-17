from utilidadescev import moeda

preco = int(input('Informe o preço: R$'))
taxa_aumento = int(input('Informe a taxa de aumento (%): '))
taxa_desconto = int(input('Informe a taxa de desconto (%): '))
moeda.resumo(preco, taxa_aumento, taxa_desconto)
