d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodado? '))
p = (d * 60) + (km * 0.15)
print('O total a pagar é: {:.2f} reais.'.format(p))