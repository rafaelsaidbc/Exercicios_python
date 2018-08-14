'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número digitado for negativo.'''
contador = 1
produto = 1
n = 0
while n >= 0:
    n = int(input('Digite um número positivo para saber sua tabuada ou um número negativo para encerrar: '))
    if n < 0:
        break
    while contador <= 10:
        produto = contador * n
        print(f'{n} * {contador} = {produto}')
        contador += 1
    contador = 1
print('FIM!')
