frase = str(input('Digite uma frase qualquer: ')).lower().strip()
a = frase.count('a')
a1 = frase.find('a') + 1  # +1 para mostrar a contagem começando de 1 e não de 0
a_ultimo = frase.rfind('a') + 1
print('Tem {} a na frase. O primeiro está na posição {} e o último está na posição {}.'.format(a, a1, a_ultimo))
