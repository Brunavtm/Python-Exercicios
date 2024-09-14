from random import randint
print('-=' * 20)
print('Vamos jogar PAR ou ÍMPAR')
print('-=' * 20)
soma = cont = 0
while True:
    v = int(input('Digite um valor: '))
    op = str(input('PAR ou ÍMPAR? [P/I]')).strip().upper()[0]
    print('-' * 20)
    comp = randint(0, 10)
    soma = v + comp
    if op == 'P' and soma % 2 == 0:
        cont += 1
        print(f'Você jogou {v} e o Computador jogou {comp} total de {soma}, que é PAR, você VENCEU!')
        print('Vamos jogar novamente...')
    if op == 'P' and soma % 2 == 1:
        print(f'Você jogou {v} e o Computador jogou {comp} total de {soma}, que é ÍMPAR, você PERDEU!')
        break
    if op == 'I' and soma % 2 == 1:
        cont += 1
        print(f'Você jogou {v} e o Computador jogou {comp} total de {soma}, que é ÍMPAR, você VENCEU!')
        print('Vamos jogar novamente...')
    if op == 'I' and soma % 2 == 0:
        print(f'Você jogou {v} e o Computador jogou {comp} total de {soma}, que é PAR, você PERDEU!')
        break
print(f'Game over. Você venceu {cont} vezes.')

