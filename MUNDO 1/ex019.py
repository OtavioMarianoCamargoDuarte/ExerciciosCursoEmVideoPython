from random import choice

aluno_1 = input('\033[31mAluno 1: ')
aluno_2 = input('\033[32mAluno 2: ')
aluno_3 = input('\033[33mAluno 3: ')
aluno_4 = input('\033[34mAluno 4: ')
print('\033[m')

lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista)

print('O aluno escolhido foi \033[4;35m{}\033[m'.format(escolhido))
