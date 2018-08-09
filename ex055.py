'''Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0
for variavel in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(variavel)))
    if variavel == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso digitado foi {}kg e o menor {}kg'.format(maior, menor))
