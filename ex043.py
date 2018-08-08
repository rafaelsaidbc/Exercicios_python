'''Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre um dos status:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 a 30: sobrepeso
- 30 a 40: obesidade
- acima de 40: obesidade mórbida'''
peso = float(input('Qual o peso da pessoa? '))
altura = float(input('Qual a altura da pessoa? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Com um IMC de {:.2f} você está abaixo do peso ideal.'.format(imc))
elif 18.5 < imc < 25:
    print('Com um IMC de {:.2f} o seu peso está ideal.'.format(imc))
elif 25 < imc < 30:
    print('Com um IMC de {:.2f} você está com sobrepeso'.format(imc))
elif 30 < imc < 40:
    print('Com um IMC de {:.2f} você está obeso.'.format(imc))
else:
    print('Com um IMC de {:.2f} você está com obesidade mórbida.'.format(imc))
