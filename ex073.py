times = ('Atlético MG', 'Palmeiras', 'Flamengo', 'Corinthias',
         'Fortaleza', 'Bragantino', 'Internacional', 'Fluminense',
         'Athletico PR', 'Atlético GO', 'Cuiabá', 'Ceará SC',
         'Sao Paulo', 'América MG', 'Juventude', 'Santos', 'Bahia',
         'Grêmio', 'Sport Recife', 'Chapecoense')
print('-=' * 25)
print(f'Lista dos 20 primeiros times do Brasileirão 2021: {times}')
print('-=' * 25)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-=' * 25)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('-=' * 25)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 25)
print('O time do Chapecoense está na {} posição.'.format(times.index('Chapecoense') + 1))
print('-=' * 25)
