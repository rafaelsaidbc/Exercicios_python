'''Crie uma tupla com os 20 primeiros colocados da Tabela do Brasileirão, na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados;
b) os últimos 4 colocados da tabela;
c) uma lista com os times em ordem alfabética;
d) em qe posição na tabela está o time da Chapecoense'''
print('-' * 50)
print('{:^50}'.format('Bem-vindos ao Brasileirão 2018'))
print('-' * 50)
brasileirão = ('São Paulo', 'Flamengo', 'Internacional', 'Grêmio', 'Atlético-MG', 'Palmeiras',
               'Corinthians', 'Cruzeiro', 'Fluminense', 'Botafogo', 'América-MG', 'Bahia',
               'Chapecoense', 'Sport', 'Vasco', 'Vitória', 'Santos', 'Ceará', 'Atlético-PR',
               'Paraná')
print('Estes são os times que disputam a Séria A do Brasileirão em 2018:\n', brasileirão)
print('-' * 50)
primeiros_cinco = brasileirão[0:5]
print('Os primeiros 5 colocados do Brasileirão são: ', primeiros_cinco)
print('-' * 50)
rebaixados = brasileirão[-4:]
print('Os últimos 4 colocados, que serão rebaixados são: ', rebaixados)
print('-' * 50)
ordem_alfabetica = sorted(brasileirão)
print('A lista de times que estão disputando o Brasileirão, em ordem alfabética é:\n', ordem_alfabetica)
print('-' * 50)
chapecoense = (brasileirão.index('Chapecoense') + 1)
print(f'A Chapecoense está na {chapecoense}ª posição.')
print('-' * 50)
print('{:^50}'.format('Volte sempre!'))
print('-' * 50)
