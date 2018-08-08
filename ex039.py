'''Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar;
- se esta na idade de se alistar;
- se já passou da idade de se alistar
O programa também deverá mostrar o tempo que falta ou que passou'''
import datetime

ano_nascimento = int(input('Qual o ano do seu nascimento? '))
idade = (datetime.date.today().year - ano_nascimento)
if idade < 18:
    print('Ainda faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar imediatamente.')
else:
    print('Você está atrasado {} anos para o alistamento.'.format(idade - 18))
