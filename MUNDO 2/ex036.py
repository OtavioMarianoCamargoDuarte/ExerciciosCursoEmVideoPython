from time import sleep

# Declarando variáveis e criando um MENU
print(' \033[1;32;43mEMPRÉSTIMOS BANCO DO BRASIL\033[m '.center(63, '='))
valor_casa = float(input('Valor da Casa: R$'))
salario = float(input('Salário do Comprador: R$'))
anos = float(input('Quantos Anos a Casa Será Paga: '))
print('='*50)

qtd_prestacoes = anos * 12
valor_prestacoes = valor_casa / qtd_prestacoes
trinta_porcent_salario = salario * 0.30

print('\033[1;35m... CALCULANDO EMPRÉSTIMO ...\033[m'.center(60))
print('='*50)
sleep(3)
if valor_prestacoes <= trinta_porcent_salario:
    print('\033[1;32mEMPRÉSTIMO APROVADO!\033[m'.center(60))
    print('Valor Total da Casa: R${:.2f}\nQuantidade de Prestações: {:.0f}\nValor das Prestações: R${:.2f}'.format(
        valor_casa, qtd_prestacoes, valor_prestacoes))
    print('='*50)

else:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m'.center(60))
    print('Salário Mensal: R${:.2f}\n30% Salário: R${:.2f}\nValor da Mensalidade: R${:.2f}'.format(
        salario, trinta_porcent_salario, valor_prestacoes))
    print('='*50)
