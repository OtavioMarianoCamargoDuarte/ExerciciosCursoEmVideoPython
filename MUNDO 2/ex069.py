from time import sleep
maior_idade = homens = mulheres_menos_vinte = 0

while True:
    print('=' * 25)
    print('CADASTRO DE PESSOA'.center(25))
    print('=' * 25)
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).upper().strip()[0]
    while sexo not in ['F', 'M']:
        sexo = str(input('SEXO [F/M]: ')).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maior_idade += 1
    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while escolha not in ['S', 'N']:
        escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('=' * 25)
    print('PESSOA CADASTRADA'.center(25))
    print('=' * 25)
    if escolha == 'N':
        sleep(1)
        print(' Programa Finalizado '.center(25, '='))
        print('=' * 25)
        break
print(' DADOS CADASTRAIS '.center(25, '='))
print(f'{maior_idade} pessoas tem +18 anos.\n{homens} homens foram cadastrados.\n{mulheres_menos_vinte} mulheres menor de 20 anos.')
print('=' * 25)
