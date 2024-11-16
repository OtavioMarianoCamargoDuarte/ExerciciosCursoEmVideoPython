'''
<<<< AULA FUNÇÕES >>>>
**************************************************************************************************************************************************

>> Interactive Help
    > Comandos:
        help()
            help(print)
            help(input)
            help(len)
            help(quit)
            print(input.__doc__)

>> docstrings
    > Comandos:
        def contador(i, f, p):

            """
            -> Faz uma contagem e mostra na tela. 
            :param i: Início da contagem
            :param f: fim da contagem
            :param p: razão da contagem
            :return: sem retorno
            Função criada por Otavio
            """
            c = i
            while c <= f
                print(f'{c}', end='..')
                c += p
            print('FIM!')

            contador(2, 10, 2)
        help(contador)

>> Argumentos opcionais
    > Comandos
        def somar(a=0, b=0, c=0): # Caso não seja informado valor de A, B ou C (A=0, B=0, C=0)
            s = a + b + c
            print(f'A soma vale {s}')
        
        somar(3, 2, 5)
        somar(8, 4)
        somar()

>> Escopo de variáveis
    > Variável Global
        > global (variavel) #deixa de criar uma variavel local para utilizar a variavel global
    > Variável Local

>> Retorno de Resultados
    > Comandos
        def somar(a = 0, b = 0, c = 0)
            s = a + b + c
            return s

        r1 = somar(3, 2, 5)
        r2 = somar(1, 7)
        r3 = somar(4)
        print(f'Meus resultados deram {r1}, {r2}, {r3}')
'''
