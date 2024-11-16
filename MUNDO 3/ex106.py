def ajuda(com):
    help(com)




# Programa Principal
comando = ''
while True:
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)