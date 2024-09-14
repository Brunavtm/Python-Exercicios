from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analise do ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é um ano BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))



