'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimética. No final, mostre
os 10 primeiros termos dessa progressão usando WHILE.'''
numero_termos = int(input('Quantos termos terá a progressão aritmética? '))
primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
progressao_aritmetica = primeiro_termo
print(progressao_aritmetica)
while numero_termos > 1:
    progressao_aritmetica += razao
    numero_termos -= 1
    print(progressao_aritmetica)
