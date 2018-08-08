'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão:
1 - binário
2 - octal
3 - hexadecimal'''
num = int(input('Escolha um número inteiro qualquer: '))
conversor = int(input('Escolha a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\nEscolha: '))
if conversor == 1:
    print('O número {} em representação binária ficará como {}"'.format(num, bin(num)))
elif conversor == 2:
    print('O número {} em representação octal ficará como {}.'.format(num, oct(num)))
elif conversor == 3:
    print('O número {} em representação hexadecimal ficará como {}.'.format(num, hex(num)))
else:
    print('Você não escolheu nenhuma das opções possíveis, tente novamente.')
