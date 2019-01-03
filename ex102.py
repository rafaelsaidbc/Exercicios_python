def fatorial(num):
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    return f'O fatorial de {num} é {fat}!'


print(fatorial(int(input('Digite um número para saber seu fatorial: '))))
