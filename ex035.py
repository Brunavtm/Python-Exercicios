print('-=' * 20)
print('      ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem FORMAR TRIÂNGULO.')
else:
    print('Os segmentos acima NÃO podem formar triângulo.')