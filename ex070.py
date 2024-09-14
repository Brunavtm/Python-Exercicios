print('_' * 20)
print('Lojas Viana')
print('_' * 20)
soma = mil = quant = menor = 0
mprod = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    soma += preço
    quant += 1
    if preço > 1000:
        mil += 1
    if quant == 1:
        menor = preço
        mprod = nome
    else:
        if preço < menor:
            menor = preço
            mprod = nome
    cad = ' '
    while cad not in 'SN':
        cad = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cad == 'N':
        break
print(f'O total da compra foi R$ {soma:.2f}.')
print(f'Temos {mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {mprod} que custou R$ {menor:.2f}')