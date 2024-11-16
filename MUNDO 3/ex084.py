pessoas = []
dados_temporarios = []
maior = menor = 0

while True:
    dados_temporarios.append(input('Nome: ').capitalize().strip())
    dados_temporarios.append(float(input('Peso: ')))

    # VERIFICANDO MAIOR E MENOR
    if len(pessoas) == 0:
        maior = menor = dados_temporarios[1]
    else:
        if dados_temporarios[1] > maior:
            maior = dados_temporarios[1]
        if dados_temporarios[1] < menor:
            menor = dados_temporarios[1]

    pessoas.append(dados_temporarios[:])
    dados_temporarios.clear()

    escolha = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if escolha == 'N':
        break

print('=' * 50)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de ', end = '')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}kg. Peso de ', end = '')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end = '')
print()
