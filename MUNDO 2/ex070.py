total_gasto = qtd_mais_mil = cont = 0
mais_barato = preco_mais_barato = float('inf')

while True:
    nome_produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco_produto = float(input('Preço: R$'))
    cont += 1

    if preco_produto < preco_mais_barato:
        mais_barato = nome_produto
        preco_mais_barato = preco_produto

    total_gasto += preco_produto

    if preco_produto > 1000:
        qtd_mais_mil += 1
    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in ['S', 'N']:
        escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        print('FINALIZANDO PROGRAMA ...')
        break

print(f'TOTAL GASTO R${total_gasto:.2f}')
print(f'{qtd_mais_mil} PRODUTOS CUSTAM MAIS DE R$1000,00')
print(f'O MAIS BARATO FOI {mais_barato} CUSTANDO R${preco_mais_barato:.2f}')