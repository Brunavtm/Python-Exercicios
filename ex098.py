"""Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que
realizar três contagens através da função criada:  a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2 c) uma contagem personalizada"""
from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1
    if i < f:
        print('=' * 30)
        print(f'Contagem de {i} a {f} de {p} em {p}:')
        for c in range(i, f + 1, p):
            print(f'{c} ', end='')
            sleep(0.5)
        print('Fim!')

    else:
        print('=' * 30)
        print(f'Contagem de {i} a {f} de {p} em {p}:')
        for c in range(i, f - 1, - p):
            print(f'{c} ', end='')
            sleep(0.5)
        print('Fim!')

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 30)
print('Agora é a sua vez de personalizar a contagem!!!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
