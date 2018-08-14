'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint

jogador = ''
jogada_jogador = 0
computador = 0
par = 'P'
impar = 'I'
jogadas = 0
while True:
    jogador = str(input('Você quer par ou ímpar [Digite P/I]? ').upper().strip())
    jogada_jogador = int(input('Qual o valor que você vai jogar? '))
    computador = randint(0, 10)
    total = jogada_jogador + computador
    if jogador == par and (jogada_jogador + computador) % 2 == 0:
        print(f'Você jogou {jogada_jogador} e o computador {computador}, o total deu {total}')
        print('O jogador venceu.')
        jogadas += 1
    elif jogador == impar and (jogada_jogador + computador) % 2 != 0:
        print(f'Você jogou {jogada_jogador} e o computador {computador}, o total deu {total}.')
        print('O jogador venceu.')
        jogadas += 1
    else:
        print(f'Você jogou {jogada_jogador} e o computador {computador}, o total deu {total}.')
        print('O computador venceu.')
        jogadas += 1
        break
        jogador = str(input('Você quer par ou ímpar [Digite P/I]? ').upper().strip())
        jogada_jogador = int(input('Qual o valor que você vai jogar? '))
        computador = randint(0, 10)
print(f'Foram necessárias {jogadas} jogadas para você perder.')
