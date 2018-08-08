'''Programa que leia o nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: sênior
- acima de 20 anos: master'''
import datetime

ano_nascimento = int(input('Qual o ano de nascimento do atleta: '))
idade = datetime.date.today().year - ano_nascimento
if idade <= 9:
    print('Atleta é da categoria MIRIM.')
elif 10 < idade <= 14:
    print('Atleta da categoria INFANTIL.')
elif 15 < idade <= 19:
    print('Atleta da categoria  JÚNIOR.')
elif idade == 20:
    print('Atleta da categoria SÊNIOR.')
else:
    print('Atleta da categoria MASTER.')
