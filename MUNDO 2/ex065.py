resp = 'S'
soma = cont = media = maior = menor = 0

while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média entre eles é: {}'.format(cont, media))
print('Maior: {} // Menor: {}'.format(maior, menor))
