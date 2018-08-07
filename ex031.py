distancia = float(input('Qual a distância sa sua viagem? '))
if distancia <= 200:
    print('Sua viagem custará R${:.2f}'.format(distancia * 0.50))
else:
    print('Sua viagem custará R${:.2f}'.format(distancia * 0.45))
