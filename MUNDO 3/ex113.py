def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[34mO usuário decidiu não fornecer mais dados.\033[m')
            return 0
        else:
            return n


def leiFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[34mO usuário decidiu não fornecer mais dados.')
            return 0
        else:
            return n


# Programa Principal
num_i = leiaInt('Digite um número inteiro: ')
num_r = leiFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {num_i} e o real {num_r}')

