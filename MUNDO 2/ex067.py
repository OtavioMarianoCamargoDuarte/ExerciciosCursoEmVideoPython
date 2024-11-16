while True:
    print('-'*20)
    numero = int(input('Informe o número para ver sua tabuada: '))
    print('-'*20)
    if numero < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{numero} x {cont:2} = {numero * cont}')
        cont += 1
