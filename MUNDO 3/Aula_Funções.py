'''
<<<< AULA FUNÇÕES >>>>

def mostrarLinha():
    print('-----------------------------------------')  # Cria uma função para mostrar uma linha

# EM VEZ DE SEMPRE FICAR ESCREVENDO print('-----------------------------------------'), vamos escrever o nome da funçao. PORTANTO...

mostrarLinha():
print('SISTEMA DE ALUNOS)
mostrarLinha():

mostrarLinha():
print('CADASTRO DE FUNCIONÁRIOS')
mostrarLinha():

mostrarLinha():
print('ERRO DO SISTEMA')
mostrarLinha():
**************************************************************************************************************************************************

def mensagem(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)

mensagem('SISTEMA DE ALUNOS')
mensagem('APRENDA PYTHON')

# RETORNA

==============================
SISTEMA DE ALUNOS
==============================
==============================
APRENDA PYTHON
==============================

**************************************************************************************************************************************************

# EMPACOTAR PARAMETROS
def contador(* num):   # * significa DESEMPACOTAR (Vários parametros jogados para dentro de num)
    for valor in num:
        print(valor, end='')
    print('FIM!')


contador(5,7,3,1,4)
contador(8,4,7)

**************************************************************************************************************************************************


'''
