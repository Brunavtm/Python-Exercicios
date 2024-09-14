lista = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if op == 'N':
        break
print('-=' * 30)
elementos = len(lista)
lista.sort(reverse=True)
print(f'Você digitou {elementos} elementos.')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 nao está na lista.')

