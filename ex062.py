'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimética. No final, mostre
os 10 primeiros termos dessa progressão usando WHILE. Pergunte ao usuário se ele deseja mostrar mais termos.
Encerre o programa se o usurário disser que quer mostrar 0 termos.'''
primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Qual será a razão da Progressão Aritmética? '))
termo = primeiro_termo
progressao_aritmetica = 1
total = 0
mais_termos = 10
while mais_termos != 0:
    total += mais_termos
    while progressao_aritmetica <= total:
        print(termo)
        termo += razao
        progressao_aritmetica += 1
    mais_termos = int(input('Digite mais quantos termos você deseja ver: '))
print('Acabou...')
