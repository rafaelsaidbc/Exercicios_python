'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores. Maioridade = 21 anos'''
import datetime

maiores = 0
menores = 0
ano_atual = datetime.date.today().year
for variavel in range(1, 8):
    ano_nascimento = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(variavel)))
    if ano_atual - ano_nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print('Você digitou o ano de {} pessoas que já atingiram a maioridade e {} pessoas que não atingiram a maioridade.'
      .format(maiores, menores))
