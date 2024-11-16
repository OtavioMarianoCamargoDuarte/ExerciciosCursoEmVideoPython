def notas(*notas, sit=False):
    """
     Calcula diversas informações sobre um conjunto de notas.

    Parâmetros:
        *notas (float): Uma ou mais notas dos alunos (aceita múltiplos valores).
        sit (bool, opcional): Indica se a situação da turma será incluída no resultado. 
                              Padrão é False.

    Retorna:
        dict: Um dicionário contendo as seguintes informações:
            - 'total': Quantidade de notas fornecidas.
            - 'maior': Maior nota entre as fornecidas.
            - 'menor': Menor nota entre as fornecidas.
            - 'média': Média das notas fornecidas.
            - 'situação' (opcional): Situação da turma, baseada na média:
                - 'BOA': Se a média for maior ou igual a 7.
                - 'RAZOÁVEL': Se a média for maior ou igual a 5 e menor que 7.
                - 'RUIM': Se a média for menor que 5.
    """
    r = {}
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas) / len(notas)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 3, 5, sit=True)
print(resp)
help(notas)
