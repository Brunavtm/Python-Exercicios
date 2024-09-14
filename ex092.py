from datetime import date
cad = dict()
cad['nome'] = str(input('Nome: '))
cad['ano de nascimento'] = int(input('Ano de nascimento: '))
cad['idade'] = date.today().year - cad['ano de nascimento']
cad['carteira de trabalho'] = str(input('Carteira de trabalho: (Se não tiver digite 0) '))
if cad['carteira de trabalho'] != '0':
    cad['ano de contratação'] = int(input('Ano de contratação: '))
    cad['salario'] = float(input('Salário: '))
    cad['aposentadoria'] = (cad['ano de contratação'] + 35) - cad['ano de nascimento']
del cad['ano de nascimento']
print('-=' * 30)
for k, v in cad.items():
    print(f'- {k} tem o valor {v}')