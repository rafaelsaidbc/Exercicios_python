'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep


def maior(*num):
    cont = maior = 0
    print('*' * 40)
    print('Analisando os valores informados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print()
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}!')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(1, 5, 46, 687, 65465, 5872, 324658)
maior(0, 6, 2, 4)
maior(1, -1, 0)
maior(1)
maior()
print("FIM!")
