soma = cont = 0
while True:
    numero = int(input('Informe um número: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi: {soma}.')