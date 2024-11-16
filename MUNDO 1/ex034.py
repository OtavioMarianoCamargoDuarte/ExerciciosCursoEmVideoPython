salario_Inicial = float(input('Informe o salário: R$'))

if salario_Inicial > 1250:
    aumento = salario_Inicial * 0.10
    salario_Final = aumento + salario_Inicial
else:
    aumento = salario_Inicial * 0.15
    salario_Final = aumento + salario_Inicial

print('Salário Inicial: R${:.2f}\nAumento: R${:.2f}\nSalário Final: R${:.2f}'.format(
    salario_Inicial, aumento, salario_Final))
