'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiro elementos de uma
sequência de Fibonacci.'''
print('*' * 30)
print('Sequência de Fibonacci.')
print('*' * 30)
n = int(input('Digite quantos termos você deseja ver da Sequência de Fibonacci: '))
t1 = 0  # o primeiro termo da sequencia sempre sera 0
t2 = 1  # o segundo termo da sequencia sempre sera 1
contador = 3  # o contador inicia a partir do terceiro termo da sequencia
print('O 1º termo da sequência é 0\nO 2º termo da sequência é 1')
while contador <= n:  # enquanto o contador for menor ou igual ao n numero de termos informado pelo usuario executa
    t3 = t1 + t2  # o termo será calculado somando os dois últimos termos
    t1 = t2  # atualiza o t1 para ser o penúltimo termo calculado
    t2 = t3  # atualiza o t2 para ser o último termo calculado
    print('O {}º termo da sequência é {}.'.format(contador, t3))
    contador += 1  # incrementa o contador até chegar ao n informado pelo usuário
print('FIM!')
