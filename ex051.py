'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimética. No final, mostre
os 10 primeiros termos dessa progressão.'''
t1 = int(input('Digite o primeiro termo da progressão aritmetica: '))
razão = int(input('Digite a razão da progressão aritmética: '))
decimo_termo = t1 + (10 - 1) * razão
for variavel in range(t1, (decimo_termo + razão), razão):
    print('{}'.format(variavel), end=' > ')
print('FIM!')
