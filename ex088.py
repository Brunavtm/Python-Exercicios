from random import randint
from time import sleep
jogos = [[], [], [], [], [], []]
print('-' * 30)
print(f'Gerador de Jogos da Mega')
print('-' * 30)
num = int(input('Quantos jogos você quer sortear? '))
sleep(0.5)
print('Sorteando os jogos')
for c in range(1, num + 1):
    print(f'Jogo {c}:', end='')
    for n in jogos:
        n = randint(1,60)
        if n not in jogos:
            print(f'[{n}]',end='')
    sleep(0.5)
    print()
