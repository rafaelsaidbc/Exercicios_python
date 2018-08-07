velocidade = float(input('Qual a velocidade do carro? '))
if velocidade <= 80:
    print('Você está dentro da lei...')
else:
    print(
        'Você estava a {} km/h e foi multado. O valor da multa é R${:.2f}'.format(velocidade, ((velocidade - 80) * 7)))
