nome = input('Qual o seu nome completo? ')
nome_lower = nome.lower()
nome_split = nome_lower.split()
if 'silva' in nome_split:
    print('Você é da família Silva.')
else:
    print('Você não é da família Silva.')
print('Outra forma de fazer')
pessoa = str(input('Qual seu nome completo? ')).strip()
print('Tem Silva no seu nome? {}'.format('silva' in pessoa.lower()))
