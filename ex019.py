import random
aluno1 = input('Qual o nome do 1º aluno? ')
aluno2 = input('Qual o nome do 2º aluno? ')
aluno3 = input('Qual o nome do 3º aluno? ')
aluno4 = input('Qual o nome do 4º aluno? ')
alunos = [aluno1, aluno2, aluno3, aluno4]
escolha = random.choice(alunos)
print('E o grande felizardo para ajudar o professor foi {}'.format(escolha))
