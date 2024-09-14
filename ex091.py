from random import randint
jogada = dict()
for c in range(0,4):
    dado = randint(1, 6)
    jogada[f'jogador{c}'] = dado
print('Valores Sorteados:')
for j, d in jogada.items():
    print(f'O {j} tirou {d} no dado.')
print('  == ORDEM DOS JOGADORES ==  ')
