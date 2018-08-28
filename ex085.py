'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
numeros = [[], []]
for numero in range(0, 7):
    num = int(input(f'Informe o {numero+1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'A lista original digitada foi {numeros}.')
numeros[0].sort()
print(f'Os números pares digitados foram {numeros[0]}.')
numeros[1].sort()
print(f'Os números ímpares digitados foram {numeros[1]}.')
