'''
( ) - TUPLA
[ ] - LISTA // dados = list()
{ } - DISCIONARIO // dados = dict()

*************************************************************************
----- EXEMPLO -----
dados = dict()
dados = {'nome':'Pedro, 'idade':25}
print(dados['nome'])   -> Pedro
print(dados['idade'])  -> 25
-------------------

dados['sexo'] = 'M'    # Cria um elemento 'sexo' e adciona o dado 'M'
del dados['idade']     # Elimina o elemento e o dado

----- EXEMPLO -----
filme = {'titulo':'Star Wars',
'ano':'1977'
'diretor':'George Lucas'
}

print(filme.values())  # Retorna todos os valores ('Star Wars', '1977', 'George Lucas')
print(filme.keys())    # Retorna as chaves ('titulo', 'ano', 'diretor')
print(filme.items())   # Retorna tanto valores quanto as chaves

for k, v in filme.items():
    print(f'O {k} é {v}')   #Retorna O 'titulo' é 'Star Wars' // O 'ano' é '1977' // O 'diretor' é 'George Lucas'
-------------------

----- EXEMPLO -----
pessoas = {'nome':'Gustavo',
'sexo':'M'
'idade':22
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')   # Usar " " quando for usar um print formatado
-------------------

----- EXEMPLO -----
brasil = []
estado_1 = {'UF':'Rio de Janeiro', 'sigla':'RJ
}
estado_2 = {'UF':'São Paulo', 'sigla':'SP'
}
brasil.append(estado_1)
brasil.append(estado_2)

print(brasil[0])     # Retorna o dicionario (estado_1)
print(brasil[1])     # Retorna o dicionario (estado_2)

print(brasil[0]['uf'])       # Retorna Rio de Janeiro
print(brasil[1]['sigla'])    # Retorna SP
-------------------

----- EXEMPLO -----
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
-------------------

'''