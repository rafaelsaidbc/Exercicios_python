'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
 você deve mostrar, para cada palavra, quais são as suas vogais.'''
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
         'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for elemento in tupla:
    print(f'\nNa palavra {elemento} temos ', end='')
    for letra in elemento:
        if letra.lower() in 'aeiou':
            print(f'\033[1;41;30m{letra}\033[0;30m', end=' ')
