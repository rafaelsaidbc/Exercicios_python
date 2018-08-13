'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digite um número inteiro qualquer: '))
opcao = 0
while opcao != 5:
    opcao = int(input('Selecione uma opção: \n[1] Somar os números\n[2] Multiplicar os números'
                      '\n[3] Mostrar o maior\n[4] Digitar novos números\n[5] Sair do programa\n'))
    if opcao == 1:
        soma = num1 + num2
        print('Você selecionou a opção [1]. A soma dos dois números é: {}'.format(soma))
    if opcao == 2:
        produto = num1 * num2
        print('Você selecionou a opção [2]. O produto dos dois números é: {}'.format(produto))
    if opcao == 3:
        if num1 > num2:
            print('Você selecionou a opção [3]. O maior número é {}.'.format(num1))
        elif num2 > num1:
            print('Você selecionou a opção [3]. O maior número é {}'.format(num2))
        else:
            print('Você selecionou a opção [3]. Porém, os números são iguais.')
    if opcao == 4:
        print('Você começará novamente.')
        num1 = int(input('Digite um número inteiro qualquer: '))
        num2 = int(input('Digite um número inteiro qualquer: '))
    if opcao == 5:
        print('Finalizando...')
print('O programa terminou')
