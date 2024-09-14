'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado'''

def ficha(nome='<desconhecido>' , num=0):
    print(f'O jogador {nome} fez {num} gol(s) no campeonato.')

nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite quantos gols ele fez: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(num=gols)
else:
    ficha(nome, gols)