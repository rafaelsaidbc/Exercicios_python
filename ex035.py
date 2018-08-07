l1 = float(input('Dê a medida de uma reta: '))
l2 = float(input('Dê a medida de outra reta: '))
l3 = float(input('Dê a medida de uma terceira reta: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
    print('As retas de comprimento {}, {} e {} podem formar um triângulo.'.format(l1, l2, l3))
else:
    print('As retas de comprimento {}, {} e {} não podem formar um triângulo.'.format(l1, l2, l3))
