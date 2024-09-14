lista = list()
mai = men = 0
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0:
        lista.append(num)
        mai = men = num
        print('Valor adicionado ao final da lista...')
    if c == 1:
        if num > mai:
            lista.append(num)
            mai = num
            print('Número adicionado ao final da lista...')
        else:
            men = num
            lista.insert(0, num)
            print('Número adicionado na posição 0...')
    if c == 2:
        if num > mai:
            lista.append(num)
            mai = num
            print('Número adicionado ao final da lista...')
        elif num < mai and num > men:
            lista.insert(1, num)
            print('Número adicionado na posição 1...')
        elif num < men:
            men = num
            lista.insert(0, num)
            print('Número adicionado na posição 0...')
    if c == 3:
        if num > mai:
            lista.append(num)
            mai = num
            print('Número adicionado ao final da lista...')
        elif num < mai and num > men and num > lista[1]:
            lista.insert(2, num)
            print('Número adicionado na posição 2...')
        elif num < mai and num > men and num < lista[1]:
            lista.insert(1, num)
            print('Número adicionado na posição 1...')
        elif num < men:
            men = num
            lista.insert(0, num)
            print('Número adicionado na posição 0...')
    if c == 4:
        if num > mai:
            lista.append(num)
            mai = num
            print('Número adicionado ao final da lista...')
        elif num < men:
            men = num
            lista.insert(0, num)
            print('Número adicionado na posição 0...')
        elif num < mai and num > men and num < lista[1]:
            lista.insert(1, num)
            print('Número adicionado na posição 1...')
        elif num < mai and num > men and num > lista[1] and num < lista[2]:
            lista.insert(2, num)
            print('Número adicionado na posição 2...')
        elif num < mai and num > men and num > lista[2]:
            lista.insert(3, num)
            print('Número adicionado na posição 3...')
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
