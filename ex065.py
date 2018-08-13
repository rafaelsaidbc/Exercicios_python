'''Crie um programa qe leia vários números inteiros no teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.'''
cont = soma = maior = menor = 0
parada = ''
while parada in 'S':
    num = int(input('Qual o número? '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    parada = str(input('Você quer digitar um número? [S/N]').upper())
media = soma / cont
print(
    'Você digitou {} números, a média entre eles é {}. O maior número digitado foi {} e o menor {}.'.format(cont, media,
                                                                                                            maior,
                                                                                                            menor))
