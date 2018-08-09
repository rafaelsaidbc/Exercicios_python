'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''
num = int(input('Digite um número para saber se é primo: '))
for variavel in range(0, 1):
    if (num != 2 and num % 2 == 0) or (num != 3 and num % 3 == 0) or (num != 5 and num % 5 == 0):
        nao_primo = num
        print('O número {} não é primo.'.format(nao_primo))
    else:
        e_primo = num
        print('O número {} é primo.'.format(e_primo))

print('Outra forma de fazer\n')
numero = int(input('Digite um número para saber se é primo: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        total += 1
if total == 2:
    print('É primo')
else:
    print('Não é primo')
