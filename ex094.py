lista = list()
cad = dict()
soma = list()
while True:
    cad['nome'] = str(input('Nome: '))
    cad['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
    while cad['sexo'] not in 'MF':
        print('Erro! Por favor digite M ou F.')
        cad['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
    cad['idade'] = int(input('Idade: '))
    lista.append(cad.copy())
    soma.append(cad['idade'])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-=' * 40)
print(f'A) Ao todo foram {len(lista)} pessoas cadastradas.')
media = sum(soma) / len(lista)
print(f'A média de idade é de {media:.1f}.')
for c in lista:
    if lista[c][cad['sexo'] == 'F':
        print(lista)

print(lista)
