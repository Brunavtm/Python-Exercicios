ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input('Média: '))
print('-=' * 30)
if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'
if 5 <= ficha['Média'] < 7:
    ficha['Situação'] = 'Recuperação'
if ficha['Média'] < 5:
    ficha['Situação'] = 'Reprovado'
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')
