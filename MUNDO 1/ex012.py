preco = float(input('Informe o valor R$:'))
desconto = preco - (preco * 0.05)
print('Valor total: R${:.2f}'.format(preco))
print('Valor com desconto de 5%: R${:.2f}'.format(desconto))
