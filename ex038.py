'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela:
- o rimeiro é maior
- o segundo é maior
- os dois são iguais'''
num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite outro valor inteiro: '))
if num1 > num2:
    print('O número {} é maior que {}!'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior que {}!'.format(num2, num1))
else:
    print('Os números {} e {} são iguais!'.format(num1, num2))
