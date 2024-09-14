velocidade = float(input('Qual a velocidade atual do carro?'))
multa = ((velocidade - 80) * 7)
if velocidade <= 80:
    print('Você está dentro do limite de velocidade da via.')
else:
    print('MULTADO!!! Você excedeu o limite de velocidade da via que é de 80Km/h.\nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')