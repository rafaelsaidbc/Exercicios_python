'''Desenvolva um programa que leio nome, idade e sexo de 4 pessoas. No final mostre:
- a média de idade
- qual o homem mais velho
- quantas mulheres tem menos de 20 anos'''
nome = ''
sexo = ''
idade = 0
idade_somatorio = 0
mulher = 0
mulheres_menores = 0
homem = 0
idade_homem = 0
homem_velho = ''
for variavel in range(1, 4 + 1):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(variavel)))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite [M] se or mulher ou [H] se for homem: '))
    sexo = sexo.upper()
    if sexo == 'H':
        homem += 1
    elif sexo == 'M':
        mulher += 1
    else:
        print('Você não escolheu uma opção válida')
    if sexo == 'M' and idade < 20:
        mulheres_menores += 1
    if sexo == 'H':
        if idade > idade_homem:
            idade_homem = idade
            homem_velho = nome
    idade_somatorio += idade
media = idade_somatorio / 4
print(
    'A média das idades é {} anos.\nO homem mais velho tem {} anos e se chama {}.\nTem {} mulheres com menos de 20 anos'.format(
        media, idade_homem, homem_velho, mulheres_menores))
