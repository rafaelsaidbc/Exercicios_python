cidade = input('Qual o nome da sua cidade? ')
cidade_lower = cidade.lower()
cidade_split = cidade_lower.split()
if 'santo' in cidade_split[0]:
    print('Sua cidade começa com Santo.')
else:
    print('Sua cidade não começa com santo.')
