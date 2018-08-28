'''Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta'''
from random import randint
from time import sleep

jogos = []
sorteio = []
numero_jogos = int(input('Quantos jogos você quer fazer? '))
contador = 0
while contador < numero_jogos:
    numeros = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            numeros += 1
        if numeros >= 6:
            break
    sorteio.sort()
    print(f'Jogo {contador+1}: {sorteio}')
    jogos.append(sorteio[:])
    sorteio.clear()
    contador += 1
    sleep(1)
