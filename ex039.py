from datetime import date
nasceu = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasceu
print('Quem nasceu em {} tem {} anos em {}.'.format(nasceu, idade, date.today().year))
if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade < 18:
    print('Ainda faltam {} anos para o seu alistamento.'.format((18 - idade)))
    print('Você deverá se alistar em {}.'.format(nasceu + 18))
else:
    print('Você ja deveria ter se alistado, está atrasado em {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nasceu + 18))
