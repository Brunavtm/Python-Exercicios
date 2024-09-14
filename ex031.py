distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km.'.format(distancia))
if distancia <= 200:
    calc1 = distancia * 0.5
    print('O preço da sua passagem será de R${:.2f}'.format(calc1))
else:
    calc2 = distancia * 0.45
    print('O preço da sua passagem será de R${:.2f}.'.format(calc2))
