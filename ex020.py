import random
aluno1 = input('Qual o nome do 1º aluno? ')
aluno2 = input('Qual o nome do 2º aluno? ')
aluno3 = input('Qual o nome do 3º aluno? ')
aluno4 = input('Qual o nome do 4º aluno? ')
alunos = [aluno1, aluno2, aluno3, aluno4]
ordem_apresentacao = random.shuffle(alunos, len(alunos))
print('A ordem de apresentação será {}'.format(ordem_apresentacao))
