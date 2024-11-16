dados_pessoais = {}
lista_geral = []
lista_mulheres = []
soma_idade = 0


while True:
    dados_pessoais.clear()
    dados_pessoais['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dados_pessoais['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if dados_pessoais['sexo'] in 'MF':
            if dados_pessoais['sexo'] == 'F':
                lista_mulheres.append(dados_pessoais['nome'])
            break
        print('ERRO! Digite somente M ou F.')
    dados_pessoais['idade'] = int(input('Idade: '))
    soma_idade += dados_pessoais['idade']
    lista_geral.append(dados_pessoais.copy())
    while True:
        opc = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if opc in 'SN':
            break
        print('ERRO! Digite somente S ou N.')
    if opc == 'N':
        break

print('=' * 30)

print(f'A) Foram cadastradas {len(lista_geral)} pessoas.')
media_idade = soma_idade / len(lista_geral)
print(f'B) A Média de idade das pessoas cadastradas é: {media_idade:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in lista_mulheres:
    print(f'{c} ', end='')
print()
print(f'D) Pessoas que tem a idade acima da média: ')
for c in lista_geral:
    if c['idade'] >= media_idade:
        print('    ')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<< ENCERRADO >>>>')
