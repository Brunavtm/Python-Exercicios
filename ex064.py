n = 0
soma = 0
sair = 999
while n != sair:
    n = int(input('Digite um número [999 para parar]: '))
    soma = soma + n
print('A soma dos números é: {}'.format(soma - 999))
