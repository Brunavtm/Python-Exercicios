import random
a = input('Primeiro aluno:')
b = input('Segundo aluno:')
c = input('Terceiro aluno:')
d = input('Quarto aluno:')
lista = [a, b, c, d]
print('O aluno escolhido para apagar o quadro é: {}.'.format(random.choice(lista)))