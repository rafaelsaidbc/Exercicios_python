'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues. Considere que o caixa possui cédulas de
R$50, R$20, R$10 e R$1.'''
valor = 1
cinquenta = 0
vinte = 0
dez = 0
um = 0
valor_restante = 0
while valor != 0:
    valor = int(input('Qual o valor do saque? R$'))
    cinquenta = valor // 50
    valor_restante = (valor - ((valor // 50) * 50))
    vinte = valor_restante // 20
    valor_restante = valor_restante - ((valor_restante // 20) * 20)
    dez = valor_restante // 10
    valor_restante = valor_restante - ((valor_restante // 10) * 10)
    um = valor_restante
    break
print(f'Você receberá {cinquenta} notas de R$50,00.\n'
      f'Você receberá {vinte} notas de R$20,00.\n'
      f'Você receberá {dez} notas de R$10,00.\n'
      f'Você receberá {um} notas de R$1,00.')
