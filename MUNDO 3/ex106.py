from time import sleep

def cabecalho(titulo=str, simbolo=str):
    tam = len(titulo) + 4
    print(f'{simbolo}' * tam)
    print(titulo.center(tam))
    print(f'{simbolo}' * tam)


def funcaoBiblioteca(funcao):
    sleep(1)
    cabecalho(f'Acessando o manual do comando {funcao}', '=')
    sleep(1)
    help(funcao)


while True:
    cabecalho('SISTEMA DE AJUDA PyHELP', '=')
    escolha = str(input('Função ou Biblioteca > '))
    if escolha.upper() == 'FIM':
        break
    else:
        funcaoBiblioteca(escolha)
cabecalho('ATÉ LOGO!', '=')
