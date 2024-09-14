lista = list()
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0:
        lista.append(num)
        print('O número foi adicionado ao final da lista...')
    if c == 1:
        if num > lista[0]:
            lista.append(num)
            print('O número foi adicionado ao final da lista...')
        if num < lista[0]:
            lista.insert(0, num)
            print('O número foi adicionado na posição 0...')
    if c == 2:
        if num > lista[1]:
            lista.append(num)
            print('O número foi adicionado ao final da lista...')
        if num < lista[0]:
            lista.insert(0, num)
            print('O número foi adicionado na posição 0...')
        if num < lista[1] and num > lista[0]:
            lista.insert(1, num)
            print('O número foi adicionado na posição 1...')
    if c == 3:
        if num > lista[2]:
            lista.append(num)
            print('O número foi adicionado ao final da lista...')
        if num < lista[0]:
            lista.insert(0, num)
            print('O número foi adicionado na posição 0...')
        if num < lista[1] and num > lista[0]:
            lista.insert(1, num)
            print('O número foi adicionado na posição 1...')
        if num < lista[2] and num > lista[1]:
            lista.insert(2, num)
            print('O número foi adicionado na posição 2...')
    if c == 4:
        if num > lista[3]:
            lista.append(num)
            print('O número foi adicionado ao final da lista...')
        if num < lista[0]:
            lista.insert(0, num)
            print('O número foi adicionado na posição 0...')
        if num < lista[1] and num > lista[0]:
            lista.insert(1, num)
            print('O número foi adicionado na posição 1...')
        if num < lista[2] and num > lista[1]:
            lista.insert(2, num)
            print('O número foi adicionado na posição 2...')
        if num < lista[3] and num > lista[2]:
            lista.insert(3, num)
            print('O número foi adicionado na posição 3...')
print('_=' * 30)
print(f'Os números informados em ordem foram: {lista}')