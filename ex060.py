'''Faça um programa que leio um número qualquer e mostre se fatorial'''
fatorial = 1
numero = int(input('Digite um número para saber seu fatorial: '))
num = numero
while numero > 0:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
    numero -= 1
print(fatorial)

print('*' * 20)
print('Fazendo o fatorial com FOR')
fatorial = 1
num = int(input('Digite um número para saber seu fatorial: '))
for numero in range(1, num + 1):
    fatorial *= numero
print('O fatorial de {} é {}.'.format(num, fatorial))
