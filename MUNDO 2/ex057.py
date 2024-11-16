sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input(
        'Dados inválidos!\n[M] - Masculino\n[F] - Feminino\nInforme seu sexo: ').upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
