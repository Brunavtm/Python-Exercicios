num = int(input('Digite um número: '))
resto = num % 2
if resto == 0:
    print('O número {:.0f} é PAR!'.format(num))
else:
    print('O número {:.0f} é IMPAR!'.format(num))
