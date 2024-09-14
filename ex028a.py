from random import randint
from time import sleep
comp = randint(0, 5) #faz computador PENSAR
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(3)
if jogador == comp:
    print('Parabéns! Você acertou!')
else:
    print('Você errou!')
print('Eu pensei em {} e você chutou {}.'.format(comp, jogador))


