ger = dict()
gols = list()
ger['nome'] = str(input('Nome do jogador? '))
partidas = int(input(f'Quantas partidas {ger["nome"]} jogou? '))
if 'partidas' != '0':
    for c in range(1,partidas + 1):
        gols.append(int(input(f'Quantos gols na {c}º partida? ')))
ger['gols'] = gols[:]
ger['total'] = sum(gols)
print('-=' * 40)
print(ger)
print('-=' * 40)
for k, v in ger.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 40)
print(f'O jogador {ger["nome"]} jogou {partidas} partidas.')
for j, g in enumerate(gols):
    print(f'  => Na partida {j + 1} ele fez {g} gols.')
print(f'Foi um total de {ger["total"]} gols.')

