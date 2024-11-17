def metade(preco=0, formato=False):
    """
    Calcula a metade de um valor fornecido.

    :param preco: (float, optional): O valor a ser dividido pela metade. Padrão é 0.
    :param formato: (bool, optional): Se True, retorna o valor formatado como moeda. Padrão é False.

    :return float | str: A metade do valor fornecido, formatada como moeda se 'formato' for True.
    """
    res = preco / 2
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    """
    Calcula o dobro de um valor fornecido.

    :param preco: (float, optional): O valor a ser duplicado. Padrão é 0.
    :param formato: (bool, optional): Se True, retorna o valor formatado como moeda. Padrão é False.

    :return float | str: O dobro do valor fornecido, formatado como moeda se 'formato' for True.
    """
    res = preco * 2
    return res if formato is False else moeda(res)


def aumentar(preco=0, porcent=0, formato=False):
    """
    Calcula o aumento de um valor com base em uma porcentagem.

    :param preco: (float, optional): O valor original. Padrão é 0.
    :param porcent: (float, optional): A porcentagem de aumento. Padrão é 0.
    :param formato: (bool, optional): Se True, retorna o valor formatado como moeda. Padrão é False.

    :return float | str: O valor aumentado pela porcentagem, formatado como moeda se 'formato' for True.
    """
    res = preco + (preco * porcent / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, porcent=0, formato=False):
    """
    Calcula a redução de um valor com base em uma porcentagem.

    :param preco: (float, optional): O valor original. Padrão é 0.
    :param porcent: (float, optional): A porcentagem de redução. Padrão é 0.
    :param formato: (bool, optional): Se True, retorna o valor formatado como moeda. Padrão é False.

    :return float | str: O valor reduzido pela porcentagem, formatado como moeda se 'formato' for True.
    """
    res = preco - (preco * porcent / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    Formata um valor numérico como moeda.

    :param preco: (float, optional): O valor numérico a ser formatado. Padrão é 0.
    :param moeda (str, optional): O símbolo ou texto que representa a moeda. Padrão é 'R$'.

    :return str: O valor formatado como moeda, com duas casas decimais e vírgula como separador decimal.
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaaumento=0, taxadesconto=0):
    print('=' * 40)
    print(' RESUMO DO VALOR '.center(40, '='))
    print('=' * 40)
    print(f'Valor Analisado: \t{moeda(preco)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'A metade do preço: \t{metade(preco, True)}')
    print(f'{taxaaumento}% de aumento: \t{aumentar(preco, taxaaumento, True)}')
    print(f'{taxadesconto}% de desconto: \t{diminuir(preco, taxadesconto, True)}')
    print('=' * 40)
