'''Faça uma tabuada do número escolhido pelo usuário utilizando for'''
numero = int(input('Digite um número para saber sua tabuada: '))
for variavel in range(1, 10 + 1):
    print('{} x {} = {}'.format(numero, variavel, numero * variavel))
print('Acabou a tabuada')
