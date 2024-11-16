salario = float(input('Qual o salário do funcionário? R$'))
reajuste = salario + (salario * 0.15)
print(
    'Um funcionário que recebia R${:.2f}, com 15% de reajuste, passa a receber R${:.2f}'.format(salario, reajuste))
