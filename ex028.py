print('Pensando em um número de 0 a 5!\nOk, agora é sua vez de adivinhar!')
num = int(input('Em que número de 0 a 5 eu pensei?'))
if num == 3:
    print('Você acertou!')
else:
    print('Você errou!')
print('Eu pensei no 3 e você no {}.'.format(num))