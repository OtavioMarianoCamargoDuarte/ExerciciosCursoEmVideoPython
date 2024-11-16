'''
ANSI Escape Sequence

- Sempre começa com \;
- Após vem o código que melhor funciona em Python o 033
- Ficando de inicio \033[CÓDIGODACORm
    - Exemplos
        - \033[ESTILO, TEXTO, BACKGROUND,m]
        - \033[0;33;44m]
        - print('\033[1;31;42mOlá, Mundo!\033[m')
        
- CRIANDO DISCIONARIO DE CORES
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'amarelo':'\033[33m',
'roxo':'\033[35m'}

STYLE
  0 - Sem estilo
  1 - Negrito
  4 - Sublinhado
  7 - Negative

TEXT
 30 - Branco
 31 - Vermelho
 32 - Verde
 33 - Amarelo
 34 - Azul
 35 - Roxo
 36 - Azul Piscina
 37 - Cinza

BACKGOUND
 40 - Branco
 41 - Vermelho
 42 - Verde
 43 - Amarelo
 44 - Azul
 45 - Roxo
 46 - Azul Piscina
 47 - Cinza
'''
