'''Faça um programa no qual o computador "pense" em um número entre 0 e 10. O jogador deve jogar até acertar
o número que o computador pensou. No final, mostre quantas tentativas foram necessárias para o jogador acertar.'''
from random import randint

computador = randint(0, 10)
jogador = -2
jogadas = 0
while jogador != computador:
    jogador = int(input('Escolha um número entre 0 e 10 para tentar advinhar o número que o computador pensou: '))
    if jogador != computador:
        if computador > jogador:
            print('O computador pensou em um número maior que o seu...')
        else:
            print('O computador pensou em um número menor que o seu...')
        print('Você errou. Tente novamente.')
    jogadas += 1
print('Foram necessárias {} jogadas para você vencer.'.format(jogadas))
