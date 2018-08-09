'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
import time

import emoji

for variavel in range(10, 0, -1):
    print('{}'.format(variavel))
    time.sleep(1)
print(emoji.emojize('Buuuuum...:fireworks:', use_aliases=True))
