'''Crie um programa que vai ler vários números e colocar em uma lista. No final mostre:
a)	Quantos números foram digitados;
b)	A lista de valores, ordenada de forma decrescente;
c)	Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
opcao = ''
while True:
    num = int(input('Adicione um número na lista: '))
    lista.append(num)
    opcao = str(input('Quer continuar? [S/N] ').upper().strip())
    if opcao == 'N':
        break
print(f'A lista tem {len(lista)} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O número 5 está na posição {lista.index(5)}.')
else:
    print('O número 5 não está na lista.')
