'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''
nome = input('Digite seu nome: ').title().strip()
print('\033[33m=\033[m'*60)
print(
    'Olá \033[32m{}\033[m, Seja bem vindo! É um prazer te conhecer.'.format(nome))
print('\033[33m=\033[m'*60)
