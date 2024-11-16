times_campeonato_brasileiro = ('CORINTHIANS', 'SÃO PAULO', 'PALMEIRAS', 'SANTOS', 'CHAPECOENSE', 'FLAMENGO',
                               'INTERNACIONAL', 'FLUMINENSE', 'VASCO', 'CRUZEIRO', 'ATLETICO MG', 'ATLETICO PR', 'RED BULL', 'GREMIO', 'VITÓRIA', 'SPORT', 'GUARANI', 'PONTE PRETA', 'FORTALEZA', 'CUIABA')

print('=' * 80)
print(f'LISTA DE CLUBES DO CAMPEONATO BRASILEIRO')
print('=' * 80)
print(times_campeonato_brasileiro)
print('=' * 80)
print(f'Os 5 primeiros colocados são: {times_campeonato_brasileiro[0:5]}')
print('=' * 80)
print(f'Os 4 últimos colocados são: {times_campeonato_brasileiro[-4:]}')
print('=' * 80)
print(f'{sorted(times_campeonato_brasileiro)}')
print('=' * 80)
print(f'A Chapecoense está em {
      times_campeonato_brasileiro.index('CHAPECOENSE') + 1}º COLOCADO')
print('=' * 80)
