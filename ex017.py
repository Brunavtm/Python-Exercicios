co = float(input('Qual comprimento do cateto oposto? '))
ca = float(input('Qual comprimento do cateto adjacente?'))
q = (co**2) + (ca**2)
h = q**(1/2)
print('Cateto oposto {}, cateto adjacente {}, a hipotenusa é igual a {:.2f}.'.format(co, ca, h))

