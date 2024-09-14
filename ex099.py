"""Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

def maior(*num):
    print('=' * 30)
    print('Analisando os valores informados...')
    print(f'{num}. Foram informados {len(num)} valores ao todo.')
    if num != 0:
        print(f' O maior valor informado foi {max(num)}.')

maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()