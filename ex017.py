from math import hypot
x = float(input('Qual o cateto oposto do triângulo retângulo? '))
y = float(input('Qual o cateto adjacente do triângulo retângulo? '))
hipotenusa = hypot(x, y)
print('A hipotenusa do triângulo com catetos {} e {} é igual a {:.2f}'.format(x, y, hipotenusa))
