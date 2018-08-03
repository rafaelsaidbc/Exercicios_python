salario = float(input('Qual o seu salário? '))
aumento = salario + (salario * 0.15)
print('Parabéns, hoje você recebe R${:.2f} reais, com o aumento de 15% receberá R${:.2f} reais.'.format(salario, aumento))
