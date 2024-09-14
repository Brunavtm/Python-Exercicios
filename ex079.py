valores = list()
while True:
    adc = (int(input('Digite um valor:')))
    if adc in valores:
        print('Valor duplicado, número não adicionado.')
    else:
        print('Valor adicionado com sucesso.')
        valores.append(adc)
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if decisao == 'N':
        break
valores.sort()
print(f'Os valores adicionados com sucesso em ordem foram: {valores}')

