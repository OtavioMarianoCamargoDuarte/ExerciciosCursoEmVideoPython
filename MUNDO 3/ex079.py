numeros = []

while True:
    novo_numero = (int(input('Digite um número: ')))
    if novo_numero not in numeros:
        numeros.append(novo_numero)
        print('Valor adcionado com sucesso!')
    else:
        print(f'O elemento {novo_numero} já existe na lista')

    escolha = (input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if escolha in 'N':
        break
print('=' * 40)
numeros.sort()
print(numeros)
