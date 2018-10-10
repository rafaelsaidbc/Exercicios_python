'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
a)	Quantas pessoas foram cadastradas;
b)	A média de idade do grupo;
c)	Uma lista com todas as mulheres;
d)	Um lista com todas as pessoas com idade acima da média.
'''
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, o sexo deve ser F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar[S/N]? ')).upper()
        if resp in 'SN':
            break
        print('Erro, responda S ou N.')
    if resp == 'N':
        break
print('*' * 40)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'A lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(f' ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Cabô!')
