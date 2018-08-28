'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta'''
matriz = []
linhas = []
for elemento in range(0, 9):
    num = int(input('Insira um valor para a matriz: '))
    linhas.append(num)
    if len(linhas) == 3:
        matriz.append(linhas[:])
        linhas.clear()
soma_pares = 0
soma_coluna3 = 0
maior = 0
for elemento in matriz:
    for numero in elemento:
        print(f'[{numero:^5}]', end=' ')
        if numero % 2 == 0:
            soma_pares += numero
    print()
    if elemento[2]:
        soma_coluna3 += elemento[2]
maior = max(matriz[1])
print(f'A soma dos elementos pares da matriz é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'O maior elemento da segunda linha é {maior}.')
