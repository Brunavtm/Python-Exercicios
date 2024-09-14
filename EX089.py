sala = list()
aluno = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    sala.append(aluno[:])
    aluno.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<5} {"Nome":^5} {"Média":>8}')
print('-'* 30)
for a, n in enumerate(sala):
    print(f'{a}      {n[0]}    {(n[1] + n[2]) / 2}')
print('-' * 30)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if notas == 999:
        break
    print(f'Notas de {sala[notas][0]} são {sala[notas][1]} e {sala[notas][2]}')
print('Finalizando...')
print('Volte Sempre!')
