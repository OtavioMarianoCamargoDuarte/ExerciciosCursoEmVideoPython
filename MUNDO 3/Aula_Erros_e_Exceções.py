'''
============================================================
                  AULA ERROS E EXECEÇÕES
============================================================

> Sintaxe;

==============================================================================

>> Algumas Exceções (Exception)
 > NameError;
 > ValueError;
 > ZeroDivisionError;
 > TypeError;
 > IndexError;
 > ModuleNotFoundError;
 > MemoryError
 > RuntimeError
 
==============================================================================

>> Comandos
> try:
    > operação
> except:
    > falhou
> else: # Opcional
    > deu certo
> finally: # Opcional
    > certo / falha

>> Mostrando o erro
> except Exception as erro:   # erro (variável)
    > print(f'Problema encontrado foi {erro.__class__}')

==============================================================================

>> EXEMPLO <<
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero.')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado.')

==============================================================================

'''