def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt}'.center(tam))
    print('~' * tam)


# PROGRAMA PRINCIPAL
escreva('GUSTAVO GUANABARA')
escreva('Curso de Python no YouTube')
escreva('CEV')
