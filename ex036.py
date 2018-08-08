'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo
será negado'''
valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = float(input('Em quantos anos a casa será quitada? '))
anos_meses = anos * 12
prestacao = valor_casa / anos_meses
if prestacao <= (salario * 0.30):
    print('O empréstimo será concedido')
    print('A prestação será de R${:.2f} por mês!'.format(prestacao))
else:
    print('\033[1;30;41mEmpréstimo negado\033[m')
    print('Infelizmente você não tem os requisitos para receber o empréstimo.')
