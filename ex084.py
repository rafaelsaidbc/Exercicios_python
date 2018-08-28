'''084 – Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
a)	Quantas pessoas foram cadastradas.
b)	Uma listagem com as pessoas mais pesadas.
c)	Uma listagem com as pessoas mais leves.
'''
temporaria = []
principal = []
menor = maior = 0
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    temporaria.append(nome)
    temporaria.append(peso)
    if len(principal) == 0:
        menor = peso
        maior = peso
    else:
        if temporaria[1] < menor:
            menor = temporaria[1]
        if temporaria[1] > maior:
            maior = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    opcao = str(input('Quer continuar? [S/N]'))
    if opcao in 'Nn':
        break
print(principal)
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'{pessoa[0]} está entre os mais leves.')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} está entre os mais pesados.')
