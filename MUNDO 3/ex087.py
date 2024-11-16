matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = terceira_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
            
        if c == 2:
            terceira_coluna += matriz[l][c]
            
        if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
            maior = matriz[1][0]
        elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
            maior = matriz[1][1]
        else:
            maior = matriz[1][2]

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)

print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior}')
