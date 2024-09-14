'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import date

def voto(ano):
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print(f' Não pode votar.')
    elif idade >= 16 and idade < 18:
        print('Voto opcional.')
    elif idade >= 18 and idade <= 70:
        print('Voto obrigatório.')
    else:
        print('Voto opcional.')


#Programa principal

ano = int(input('Digite o ano de nascimento do eleitor: '))
voto(ano)