def menu():
    '''
    Exibe o menu principal e retorna a opção escolhida.
    '''
    print("\n" + "=" * 30)
    print('SISTEMA DE CADASTRO DE PESSOAS')
    print('=' * 30)
    print('1 - Cadastrar nova pessoa')
    print('2 - Listar todas as pessoas')
    print('3 - Sair')
    print('=' * 30)
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao not in [1, 2, 3]:
            raise ValueError('Opção Inválida!')
        return opcao
    except ValueError:
        print('Por Favor, insira um número válido.')
        return 0


def mensagemSaida():
    '''
    Exibe uma mensagem ao sair do sistema.
    '''
    print('\nEncerrando o sistema... Até logo!')
