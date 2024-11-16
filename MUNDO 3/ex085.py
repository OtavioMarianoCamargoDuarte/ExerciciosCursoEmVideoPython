lista = []
pares = []
impares = []

for c in range(0, 7):
    numero = int(input(f'Digite o {c + 1}º valor: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
pares.sort()
impares.sort()

lista.append(pares[:])
lista.append(impares[:])

print(f'Os números pares são {lista[0]}')
print(f'Os números impares são {lista[1]}')
