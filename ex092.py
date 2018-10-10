'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date

dicionario = {}
ano_atual = date.today().year
dicionario['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = ano_atual - ano_nascimento
dicionario['ctps'] = int(input('Número da carteira de trabalho (0 se não tiver): '))
if dicionario['ctps'] > 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['contratação'] + 35
print(dicionario)
print('*' * 40)
for chave, valor in dicionario.items():
    if chave == 'ctps':
        if valor == 0:
            print('Não tem carteira de trabalho.')
    else:
        print(f'O campo {chave} tem o valor {valor}.')

# print(f'O nome é {dicionario["nome"]}.')
# print(f'A idade é {dicionario["idade"]}.')
# if dicionario['ctps'] > 0:
#    print(f'A CTPS é {dicionario["ctps"]}.')
#    print(f'A contratação foi em {dicionario["contratação"]}.')
#    print(f'O salário é R${dicionario["salario"]}.')
#    print(f'Vai se aposentar em {dicionario["aposentadoria"]}.')
# else:
#    print('Não tem carteira de trabalho.')
