import time
sal = float(input('Qual é o seu salário? R$ '))
print('Calculando o seu aumento...')
time.sleep(2)
if sal > 1250:
    print('O valor do seu novo salário com 10% de aumento é R$ {:.2f}.'.format(sal * 1.1))
else:
    print('O valor do seu novo salário com 15% de aumento é R$ {:.2f}.'.format(sal *1.15))
