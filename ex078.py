'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista = []
for numero in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {numero}: ')))
print(f'Os valores digitados foram {lista}')
print(f'O menor número digitado foi {min(lista)} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{indice}... ', end='')
print(f'\nO maior número digitado foi {max(lista)} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{indice}... ', end='')
