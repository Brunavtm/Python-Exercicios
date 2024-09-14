#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(a, b):
    print(f'A área de um terreno de {a} x {b} é de {a*b} m².')


print('   Controle de Terrenos ')
print('_' * 30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)

