nome = str(input('Digite seu nome completo: ')).strip()  # strip para ignorar possíveis espaços no início da digitação
nome_split = nome.split()
primeiro_nome = nome_split[0]
ultimo_nome = nome_split[-1]
print('O primeiro nome de {} é {} e o último é {}!'.format(nome, primeiro_nome, ultimo_nome))
