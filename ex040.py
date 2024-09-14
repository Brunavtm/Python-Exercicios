n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando nota {:.1f} e {:.1f} a média do aluno é {}.'.format(n1, n2, media))
if media < 5:
    print('Sua média foi {:.1f}, portanto menor que 5.0, você está REPROVADO.'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi {:.1f}, portanto entre 5.0 e 6.9, você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua média foi {:.1f}, portanto maior ou igual a 7.0, você está APROVADO.'.format(media))
