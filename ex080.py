'''Crie um programa que o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final , mostre a lista ordenada na tela.'''
lista = []
for elemento in range(0, 5):
    numero = int(input('Adicione um número na lista: '))
    if elemento == 0 or numero >= lista[-1]:
        lista.append(numero)
        print(f'O número {numero} foi adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao <= len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'O número {numero} foi inserido na posição {posicao}...')
                break
            posicao += 1
print(f'Você digitou essa lista\n{lista}')
