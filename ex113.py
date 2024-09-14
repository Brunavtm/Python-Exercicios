def leiaInt(msg):
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número real válido.\033[m')
            continue
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'O número digitado foi {num}')
num2 = leiaFloat('Digite um valor: ')
print(f'O número digitado foi {num2}')