import math
an =float(input('Informe o ângulo que você deseja: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print('O ângulo {} tem SENO {:.2f}, COSSENO {:.2f} e TANGENTE {:.2f}.'.format(an, s, c, t))