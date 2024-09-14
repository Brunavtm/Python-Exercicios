def leiaInt(n):
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            n = int(n)
            return n
            break
        else:
            print(f'\033[31mERRO, digite um número inteiro válido.\033[m')


#programa principal
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')