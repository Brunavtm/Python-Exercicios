print('-=' * 20)
print('       Aprovação de empréstimo!')
print('-=' * 20)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Salário do comprador? '))
tempo = int(input('Quantos anos de financiamento? '))
prestação = casa / (tempo * 12)
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}.'.format(casa, tempo, prestação))
if prestação > (salario * 30 / 100):
    print('Sinto muito, seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado!')