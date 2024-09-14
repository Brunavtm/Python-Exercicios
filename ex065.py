opção = ''
num = 0
cont = 0
soma = 0
maior = 0
menor = 0
while opção != 'N':
    num = int(input('Digite um número: '))
    opção = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    soma = soma + num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Você digitou {} números e a média deles é {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
