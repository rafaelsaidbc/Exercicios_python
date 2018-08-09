'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
se encontram no intervalo de 1 até 500'''
soma = 0
for variavel in range(1, 500 + 1, 2):
    if variavel % 3 == 0:
        soma += variavel
print('A soma dos números ímpares e múltiplos de 3 que existem entre 1 e 500 é \033[1;30;41m{}\033[m!'.format(soma))
