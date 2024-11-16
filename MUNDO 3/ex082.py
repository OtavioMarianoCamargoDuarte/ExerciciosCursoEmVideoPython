lista = []
pares = []
impares = []

while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    escolha = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if escolha == 'N':
        break

print(f'A lista digitada foi {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')
