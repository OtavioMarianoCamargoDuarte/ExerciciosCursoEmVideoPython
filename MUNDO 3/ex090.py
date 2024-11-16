inf_aluno = dict()

inf_aluno['Nome'] = str(input('Nome: '))
inf_aluno['Média'] = float(input('Média: '))

if inf_aluno['Média'] >= 7:
    inf_aluno['Situacão'] = 'Aprovado'
elif 5 <= inf_aluno['Média'] < 7:
    inf_aluno['Situacão'] = 'Recuperação'
else:
    inf_aluno['Situacão'] = 'Reprovado'
print('=' * 20)
for k, v in inf_aluno.items():
    print(f'{k} é igual a {v}')
