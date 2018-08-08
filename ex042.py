'''Verificar se 3 retas podem formar um triângulo e qual tipo de triângulo elas formarão
- equilátero: todos os lados são iguais
- isósceles: dois lados iguais
- escaleno: nenhum lado igual'''
lado1 = float(input('Dê a medida de uma reta: '))
lado2 = float(input('Dê a medida de outra reta: '))
lado3 = float(input('Dê a medida de uma terceira reta: '))
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado2 + lado1):
    print('As retas de comprimento {}, {} e {} podem formar um triângulo.'.format(lado1, lado2, lado3))
    if lado1 == lado2 and lado1 == lado3:
        print('O triângulo formado será EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo formado será ISÓSCELES')
    else:
        print('O triângulo formado sera ESCALENO.')

else:
    print('As retas de comprimento {}, {} e {} não podem formar um triângulo.'.format(lado1, lado2, lado3))
