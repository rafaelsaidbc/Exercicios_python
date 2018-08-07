salario = float(input('Qual o salário? '))
if salario <= 1250:
    print('O seu aumento será de 15%, você ganhará R${:.2f}'.format(salario + (salario * 0.15)))
else:
    print('O seu aumento será de 10%, você ganhará R${:.2f}'.format(salario + (salario * 0.10)))
