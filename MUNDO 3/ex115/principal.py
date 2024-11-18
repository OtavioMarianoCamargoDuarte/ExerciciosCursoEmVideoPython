import arquivo, interface


# Registrando nome do arquivo
nome_arquivo = 'cadastros.txt'


# Garantindo que o arquivo existe
arquivo.verificarArquivo(nome_arquivo)


while True:
    opcao = interface.menu()
    if opcao == 1:
        nome = input('Digite o nome da pessoa: ').strip()
        try:
            idade = int(input('Digite a idade: '))
            if idade < 0:
                raise ValueError('A idade não pode ser negativa.')
            arquivo.cadastrarPessoas(nome_arquivo, nome, idade)
            print(f'{nome} cadastrado(a) com sucesso!')
        except ValueError:
            print('Erro: A idade deve ser um número inteiro válido.')
    elif opcao == 2:
        arquivo.listarPessoas(nome_arquivo)
    elif opcao == 3:
        interface.mensagemSaida()
        break
