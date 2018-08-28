'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta'''
matriz = []
linhas = []
for elemento in range(0, 9):
    num = int(input('Insira um valor para a matriz: '))
    linhas.append(num)
    if len(linhas) == 3:
        matriz.append(linhas[:])
        linhas.clear()
for elemento in matriz:
    for numero in elemento:
        print(f'[{numero:^5}]', end=' ')
    print()
