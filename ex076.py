'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre um listagem de preços, organizando os dados em forma tabular.'''
tupla = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for elemento in range(0, len(tupla)):
    if elemento % 2 == 0:
        print(f'{tupla[elemento]:.<28}', end='')
    else:
        print(f'R${tupla[elemento]:>10.2f}')
print('-' * 40)
