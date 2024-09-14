while True:
    print('-' * 20)
    num = int(input('Digite um número para ver a tabuada: '))
    print('-' * 20)
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num:2} x {c:2} = {num * c:2}')
print('Programa de tabuada encerrado. Volte sempre!')
