from math import sin, cos, tan, radians

angulo = int(input('Informe o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('SENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(
    seno, cosseno, tangente))
