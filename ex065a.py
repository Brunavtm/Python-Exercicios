resp = 'Ss'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant+= 1
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('Você digitou {} números e a média deles é: {:.2f}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))

