import math
angulo = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
