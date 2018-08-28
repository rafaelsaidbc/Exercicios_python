'''Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = []
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos.append(nome)
    alunos.append(nota1)
    alunos.append(nota2)
    lista.append(alunos[:])
    alunos.clear()
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
print(f'{"Nº":<4} {"Nome":<20} {"Média":<5}')
print('-' * 30)
for indice, aluno in enumerate(lista):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{indice:<4} {aluno[0]:<20} {media:<5.1f} ')
print('-' * 30)
while True:
    opcao = int(input('Você quer ver as notas de qual aluno (999 encerra)? '))
    if opcao == 999:
        break
    else:
        opcao = lista[opcao]
        print(f'As notas de {opcao[0]} são {opcao[1]} e {opcao[2]}')
