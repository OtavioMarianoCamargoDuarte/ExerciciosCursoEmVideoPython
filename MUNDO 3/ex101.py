def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O VOTO É OPCIONAL!'
    else:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO!'
    

# Programa Principal
nasc = int(input('Informe a data de nascimento: '))
print(voto(nasc))


print(voto(2015))
print(voto(2008))
print(voto(1995))
print(voto(1940))
