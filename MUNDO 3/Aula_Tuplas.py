'''
( ) - TUPLA
[ ] - LISTA
{ } - DISCIONARIO

Maneiras de usar o for com TUPLAS

lanche = ('Hambuerguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

*************************************************************************
print(sorted(lanche)) #Faz mostrar os itens da tupla em ORDEM
*************************************************************************

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

## RETORNA ##
(2, 5, 4, 5, 8, 1, 2) # Junta as duas tuplas em uma só

print(c.count(5)) # Quantas vezes aparece o número 5

print(c.index(8)) # Em que posição está o número 8 "PRIMEIRA OCORRENCIA"
*************************************************************************

pessoa = ('Gustavo', 39, 'M', 99.88)

del(pessoa) #APAGA A TUPLA

'''