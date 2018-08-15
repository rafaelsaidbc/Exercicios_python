'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois
mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla.'''
import random

tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10))
print('Os números sorteados foram: ', end='')
for num in tupla:
    print(f'{num} ', end='')
print(f'\nO maior número sorteado foi: {max(tupla)}')
print(f'O menor número sorteado foi: {min(tupla)}')
