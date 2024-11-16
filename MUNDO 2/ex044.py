print('='*68)
valor_inicial = float(input('Informe o valor do produto: R$'))

# CONDIÇÕES DE PAGAMENTO #
a_vista_din_cheque = valor_inicial - (valor_inicial * 0.1)
a_vista_cartao = valor_inicial - (valor_inicial * 0.05)
duas_vezes_cartao = valor_inicial
tres_vezes_cartao = valor_inicial + (valor_inicial * 0.2)

print('='*68)
print('Pagamento à vista (R$ / Cheque): 10% OFF // \033[31mR${:.2f}\033[m >>> \033[32mR${:.2f}\033[m'.format(
    valor_inicial, a_vista_din_cheque))
print('Pagamento à vista (cartão): 5% OFF // \033[31mR${:.2f}\033[m >>> \033[32mR${:.2f}\033[m'.format(
    valor_inicial, a_vista_cartao))
print('Pagamento parcelado 2x no cartão: SEM JUROS // \033[33mR${:.2f}\033[m >>> \033[33mR${:.2f}\033[m'.format(
    valor_inicial, duas_vezes_cartao))
print('Pagamento parcelado 3x no cartão: 20% JUROS // \033[32mR${:.2f}\033[m >>> \033[31mR${:.2f}\033[m'.format(
    valor_inicial, tres_vezes_cartao))
print('='*68)
