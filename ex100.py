'''Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e
vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep
numeros = list()
soma = list()
from random import randint
def sorteia(* num):
    print(f'Sorteando 5 valores para a lista...')
    for c in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
        print(f'{num}', end=' ')
        sleep(0.3)
    print(f'Pronto!')
def somaPar():
    for c in numeros:
        if c % 2 == 0:
            soma.append(c)
    print(f'Somando os valores pares de {numeros} temos {sum(soma)}.')


sorteia()
somaPar()
