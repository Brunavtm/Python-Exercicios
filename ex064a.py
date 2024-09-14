n = 0
cont = 0
soma =0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Voce digitou {} números e a soma deles é {}.'.format(cont, soma))