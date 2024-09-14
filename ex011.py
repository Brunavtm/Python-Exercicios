l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
area = a * l
print('A altura da sua parede é: {}m, a largura é:{}m tendo portanto área igual a {}m².'.format(a, l, area))
print('Para pintar a sua parede você vai precisar de {} litros de tinta.'.format(area/2))
