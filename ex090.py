'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
dicionario = {}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
dicionario['nome'] = nome
dicionario['media'] = media
if media < 5:
    dicionario['situação'] = 'Reprovado'
elif media < 7:
    dicionario['situação'] = 'Em recuperação'
else:
    dicionario['situação'] = 'Aprovado'
print('*' * 40)
for chave, valor in dicionario.items():
    print(f' - {chave} é {valor}')
# print(f'Nome é {dicionario["nome"]}.')
# print(f'A média foi {dicionario["media"]}')
# print(f'A situação é {dicionario["situação"]}')
