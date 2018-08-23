'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitador, em ordem crescente.'''
lista = []
opcao = ''
while True:
    num = int(input('Informe um valor para ser adicionado: '))
    if num not in lista:
        lista.append(num)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado, não será adicionado...')
    opcao = str(input('Quer continuar? [S/N]').upper().strip())
    if opcao == 'N':
        break
print(f'Você digitou assim: {lista}')
lista.sort()
print(f'A lista em ordem crescente fica assim: {lista}')
