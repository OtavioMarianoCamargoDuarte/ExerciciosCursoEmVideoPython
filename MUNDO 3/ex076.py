listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

# Criação do Cabeçalho
print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40, ' '))
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)


'''print(f'{listagem[0].ljust(40, '.')}R$    {listagem[1]:.2f}')
print(f'{listagem[2].ljust(40, '.')}R$    {listagem[3]:.2f}')
print(f'{listagem[4].ljust(40, '.')}R$   {listagem[5]:.2f}')
print(f'{listagem[6].ljust(40, '.')}R$   {listagem[7]:.2f}')
print(f'{listagem[8].ljust(40, '.')}R$    {listagem[9]:.2f}')
print(f'{listagem[10].ljust(40, '.')}R$    {listagem[11]:.2f}')
print(f'{listagem[12].ljust(40, '.')}R$  {listagem[13]:.2f}')
print(f'{listagem[14].ljust(40, '.')}R$  {listagem[15]:.2f}')
print(f'{listagem[16].ljust(40, '.')}R$  {listagem[17]:.2f}')'''
