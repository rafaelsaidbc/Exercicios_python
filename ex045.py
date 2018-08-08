'''Jogo do jokempo: tesoura papel e pedra'''
import random

jogador = int(input('Selecione'
                    '\n[1] tesoura'
                    '\n[2] pedra'
                    '\n[3] papel\n'))
computador = random.randint(1, 3)
tesoura = 1
pedra = 2
papel = 3
if jogador == tesoura and computador == tesoura or jogador == pedra and computador == pedra or jogador == papel and computador == papel:
    print('Você e o computador fizeram a mesma escolha, vocês empataram.')
elif jogador == pedra and computador == papel:
    print('Você escolheu pedra e o computador papel, você perdeu.')
elif jogador == pedra and computador == tesoura:
    print('Você escolheu pedra e o computador tesoura, você ganhou.')
elif jogador == papel and computador == tesoura:
    print('Você escolheu papel e o computador escolheu tesoura, você perdeu.')
elif jogador == papel and computador == pedra:
    print('Você escolheu papel e o computador pedra, você ganhou.')
elif jogador == tesoura and computador == papel:
    print('Você escolheu tesoura e o computador papel, você ganhou.')
elif jogador == tesoura and computador == pedra:
    print('Você escolheu tesoura e o computador pedra, você perdeu.')
else:
    print('Você não escolheu uma opção válida.')
