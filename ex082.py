'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e o valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []
opcao = ''
while True:
    num = int(input('Adicione um número à lista: '))
    lista.append(num)
    opcao = str(input('Quer continuar? [S/N]').upper().strip())
    if opcao == 'N':
        break
print(f'A lista original foi: {lista}')
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os números pares da lista são: {pares}')
print(f'Os números ímpares da lista são: {impares}')
