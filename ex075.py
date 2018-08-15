'''Crie um programa que leia quatro valores informados pelo usuário e guarde-os em uma tupla.
No final mostre:
a) quantas vezes apareceu o valor 9;
b) em que posição foi digitado o primeiro valor 3;
c) quais foram os números pares.'''
tupla = (int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')))
print(f'Você digitou os números {tupla}.', end='')
nove = tupla.count(9)
print(f'\nO número 9 apareceu {nove} vezes.')
if 3 in tupla:
    tres = tupla.index(3) + 1
    print(f'A primeira vez que o número 3 apareceu foi na {tres}ª posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Você digitou os seguintes números pares ', end='')
for elemento in tupla:
    if (elemento % 2) == 0:
        print(elemento, end=' ')
