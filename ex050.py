'''Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
for variavel in range(1, 6 + 1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares digitados é \033[1;31;40m{}\033[m.'.format(soma))
