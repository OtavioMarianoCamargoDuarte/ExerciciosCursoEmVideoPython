lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    escolha = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if escolha == 'N':
        break

print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}')
if lista.count(5) == 0:
    print('Não tem o número 5 na lista.')
else:
    print(f'Temos {lista.count(5)} números 5 na lista.')
