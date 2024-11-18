def verificarArquivo(nome_arquivo):
    '''
    Verifica se o arquivo existe, caso contrario, cria-o.
    '''
    try:
        with open(nome_arquivo, 'r') as _:
            pass
    except FileNotFoundError:
        with open(nome_arquivo, 'w') as _:
            pass


def cadastrarPessoas(nome_arquivo, nome, idade):
    '''
    Cadastrar uma nova pessoa no arquivo.
    '''
    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{nome}; {idade}\n')
    except Exception as e:
        print(f'Erro ao cadastrar pessoa {e}')

def listarPessoas(nome_arquivo):
    '''
    Lê e exibe todas as pessoas cadastradas no arquivo.
    '''
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print('\nLista de pessoas Cadastradas:')
            print('-' * 30)
            for linha in arquivo:
                nome, idade = linha.strip().split(';')
                print(f'Nome: {nome:<10} Idade: {idade} anos')
            print('-' * 30)
    except Exception as e:
        print(f'Erro ao listar pessoas: {e}')