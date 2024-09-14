print(' ========= Lojas Viana ===========')
valor = float(input('Preço das compras: '))
print('''' FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro / cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Digite a opção: '))
if forma == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, valor -valor * 10 / 100))
elif forma == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, valor - valor * 5 / 100))
elif forma == 3:
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, valor))
elif forma == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${} COM JUROS.'.format(parcela, (valor + valor * 20 / 100) / parcela))
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, valor + valor * 20 / 100))

