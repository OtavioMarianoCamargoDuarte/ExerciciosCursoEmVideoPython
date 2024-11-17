'''
============================================================
                  AULA MODULOS E PACOTES
============================================================
============================================================
                        AULA MODULOS
============================================================
EXEMPLO:

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

====================================================================
COLOCO TODOS AS FUNCOES ACIMA E COLOCO DENTRO DE UM ARQUIVO UTEIS.PY
====================================================================

from uteis import fatorial, dobro, triplo    #PARA IMPORTAR AS FUNCOES FATORIAL, DOBRO e TRIPLO
OU
import uteis                                 #PARA IMPORTAR TODAS AS FUNCOES

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

============================================================
                        AULA PACOTES
============================================================
IMPORT UTEIS      #IMPORTA O PACOTE INTEIRO

TODA PASTA È UM PACOTE
BASTA IR CRIANDO PASTA DENTRO DE PASTA

EXEMPLO:

Pasta: > Uteis
        >__init__.py
            > Cores
             >__init__.py
            > Números
             > __init__.py
            > Datas
             > __init__.py
            > Strings
             > __init__.py

Sintaxe padrão 
> __init__.py    #Dentro de cada pasta terá um __init__.py
============================================================
'''