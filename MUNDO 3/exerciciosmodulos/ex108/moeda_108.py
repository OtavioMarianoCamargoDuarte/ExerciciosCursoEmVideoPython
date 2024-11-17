def metade(preco = 0):
    res = preco / 2
    return res

def dobro(preco = 0):
    res = preco * 2
    return res

def aumentar(preco = 0, porcent = 0):
    res = preco + (preco * porcent / 100)
    return res

def diminuir(preco = 0, porcent = 0):
    res = preco - (preco * porcent / 100)
    return res


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')