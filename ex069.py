h = m = g = 0
while True:
    print('_' * 20)
    print('CADASTRE UMA PESSOA')
    print('_' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('_' * 20)
    if sexo in 'M':
        h += 1
        if idade > 18:
            g += 1
    if sexo in 'F':
        if idade > 18:
            g += 1
        if idade < 20:
            m += 1
    jogar = ' '
    while jogar not in 'SN':
        jogar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if jogar == 'N':
        break
print(f'Total de {g} pessoas com mais de 18 anos cadastradas.')
print(f'Ao todo foram {h} homens cadastrados.')
print(f'Foram cadastradas {m} mulheres com menos de 20 anos.')

