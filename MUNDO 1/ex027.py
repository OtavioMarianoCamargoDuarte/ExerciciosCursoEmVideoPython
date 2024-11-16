nome = input('Digite seu nome completo: ')
sespacos = nome.strip().title()
dividido = sespacos.split()
cont = len(sespacos)

print('Seu nome é {}\nSeu primeiro nome é {} e seu último nome é {}'.format(
    sespacos, dividido[0], dividido[-1]))
