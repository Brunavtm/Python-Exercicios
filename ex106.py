'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.'''
def sis(msg):
    from time import sleep
    while True:
        c = 'SISTEMA DE AJUDA PyHELP'
        print('\033[30;42m~' * len(c), '\033[m' )
        print(f'\033[30;42m{c} \033[m')
        print('\033[30;42m~' * len(c),'\033[m')
        msg = str(input('Função ou biblioteca: '))
        0.5
        if msg == 'fim':
            print('\033[41mAté logo!\033[m')
            break
        else:
            co = f'Acessando manual do comando {msg}'
            print('\033[30;44m~' * len(co), '\033[m')
            print(f'\033[30;44m{co} \033[m')
            print('\033[30;44m~' * len(co), '\033[m')
            sleep(0.5)
            print('\033[47m')
            print(f'{help(msg)}')
            print('\033[m')


sis('msg')




