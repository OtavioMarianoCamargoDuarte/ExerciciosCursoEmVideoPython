from datetime import date

ano_atual = date.today().year

dados_pessoais = {}
print('=' * 30)
print(' CADASTRO ÚNICO '.center(30, '='))
print('=' * 30)


dados_pessoais['nome'] = str(input('Nome: ')).strip().capitalize()
ano_nascimento = int(input('Ano de Nascimento: '))
dados_pessoais['idade'] = ano_atual - ano_nascimento
dados_pessoais['carteira de trabalho'] = int(
    input('Carteira de Trabalho: (0 se não tem):'))

if dados_pessoais['carteira de trabalho'] != 0:
    dados_pessoais['contratação'] = int(input('Ano de Contratação: '))
    dados_pessoais['salário'] = float(input('Salário: R$'))
    dados_pessoais['aposentadoria'] = (
        dados_pessoais['contratação'] - ano_nascimento) + 35 + dados_pessoais['idade']
print('='*30)
for k, v in dados_pessoais.items():
    print(f'- {k} tem o valor {v}')
