peso = float(input('Qual o peso em kg: '))
altura = float(input('Qual a altura em metros: '))
imc = peso / (altura ** 2)
print('O IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está no sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
