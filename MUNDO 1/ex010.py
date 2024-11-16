real = float(input('Quantos reais você tem? '))
dollar = real / 3.27

print('Com R${:.2f} você consegue trocar por {:.2f}US$'.format(real, dollar))
