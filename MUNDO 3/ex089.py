alunos = []

while True:
    nome = input('Nome: ').capitalize().strip()
    nota_1 = float(input('1ª nota: '))
    nota_2 = float(input('2ª nota: '))
    media = (nota_1 + nota_2) / 2
    # nome -> lista[0] // nota_1 e nota_2 -> lista[1] // media -> lista[2]
    alunos.append([nome, [nota_1, nota_2], media])
    escolha = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break

print('=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MEDIA':>8}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 30)
    opc = int(input('Qual aluno quer ver as notas? (999 para finalizar): '))
    if opc == 999:
        break
    elif opc <= len(alunos) - 1:
        print(f'As notas do aluno {alunos[opc][0]} são: {alunos[opc][1]}')
print(' VOLTE SEMPRE '.center(30, '-'))
