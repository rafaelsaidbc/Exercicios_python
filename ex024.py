cidade = str(input('Qual o nome da sua cidade? '))
cidade_lower = cidade.lower()
cidade_split = cidade_lower.split()
if 'santo' in cidade_split[0]:
    print('Sua cidade começa com Santo.')
else:
    print('Sua cidade não começa com santo.')
print('Outra forma de fazer: ')
cid = str(input('Digite o nome da sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
