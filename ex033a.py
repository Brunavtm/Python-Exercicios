a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é menor:
menor = a
if b < a or b < c:
    menor = b
if c < a or c < b:
    menor = c
#verificando maior valor:
maior = a
if b > a or b > c:
    maior = b
if c > a or c > b:
    maior = c
print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))