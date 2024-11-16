from math import sqrt, hypot
'''
cat_o = float(input('Informe o Cateto Oposto: '))
cat_a = float(input('Informe o Cateto Adjacente: '))
hip = sqrt((cat_o ** 2) + (cat_a ** 2))

print('A hipotenusa do triângulo citado é: {:.2f}'.format(hip))
'''
cat_o = float(input('Informe o Cateto Oposto: '))
cat_a = float(input('Informe o Cateto Adjacente: '))
hip = hypot(cat_a, cat_o)

print('{:.2f}'.format(hip))
