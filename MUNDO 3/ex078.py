numeros = []
maior = menor = 0

for n in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {n}: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]

print('=' * 40)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...',end = '')
print()


'''maior = max(numeros)
menor = min(numeros)
posicao_maior = numeros.index(maior)
posicao_menor = numeros.index(menor)

print(f'O maior número digitado foi {
maior}, e sua posição na lista é: {posicao_maior + 1}º')
print(f'O menor número digitado foi {
menor}, e sua posição na lista é: {posicao_menor + 1}º')'''
