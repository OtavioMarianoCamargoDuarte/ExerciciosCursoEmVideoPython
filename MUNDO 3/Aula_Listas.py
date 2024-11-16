'''
( ) - TUPLA
[ ] - LISTA
{ } - DISCIONARIO

lista.append('elemento') #Adciona elemento a lista
lista.insert(0, 'elemento') #Adciona elemento em determinada posição

*************************************************************************

del.lista[3] #Apaga um elemento da lista
lista.pop(3) #Apaga um elemento da lista (Normalmente utilizado para apagar o último elemento)
lista.remove('elemento') #Apaga um elemento da lista

*************************************************************************

valores = list(range(4, 11)) #Criando uma lista atraves do comando LIST

valores.sort() #Coloca os valores organizados
valores.sort(reverse=True) #Valores ordenados em decrescente

len(lista) #Quantos elementos existem na lista

*************************************************************************

a = [2, 3, 4, 7]
b = a #Cria uma ligação entre as listas
b = a[:] #Copia a lista, porém cada uma é individual

*************************************************************************

galera = [['Joao', 19], ['Ana', 33], ['Joaquim, 13'], ['Maria', 45]]
print(galera[2][1])
## DEVOLVE
13

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

*************************************************************************

total_maior = total_menor = 0

galera = []
dados = []
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(str(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
    print(f'{p[0]} é menor de idade.')
    total_menor += 1

print(f'temos {total_maior} maiores e {total_menor} menores de idade')
'''