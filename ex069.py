'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não quer continuar. No final mostre:
a) quantas pessoas tem mais de 18 anos;
b) quantos homens foram cadastrados;
c) quantas mulheres tem menos de 20 anos.'''
idade = 0
sexo = ''
pessoas_maiores = 0
homens = 0
mulheres_menor_20 = 0
continua = ''
while True:
    print('=' * 30)
    print('Cadastro de pessoas')
    print('=' * 30)
    continua = str(input('Você quer continuar [S/N]? ').upper().strip())
    if continua == 'S':
        idade = int(input('Qual a idade da pessoa? '))
        if idade > 18:
            pessoas_maiores += 1
        sexo = str(input('Qual o sexo da pessoa [M/F]').upper().strip())
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres_menor_20 += 1
    else:
        break
print(f'Foram cadastradas {pessoas_maiores} que tem mais de 18 anos!\n'
      f'Foram cadastrados {homens} homens!\n'
      f'Foram cadastradas {mulheres_menor_20} mulheres que tem menos de 20 anos!')
