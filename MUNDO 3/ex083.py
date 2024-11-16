expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')


'''expressao = input('Digite a expressão: ')
parenteses_aberto = expressao.count('(')
parenteses_fechado = expressao.count(')')
if parenteses_aberto == parenteses_fechado:
    print(f'Sua expressão digitada foi: {expressao}\nÉ UMA EXPRESSÃO VÁLIDA!')
else:
    print(f'Sua expressão digitada não é válida.')'''
