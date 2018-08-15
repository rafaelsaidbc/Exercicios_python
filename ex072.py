'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão,
de zero até 20. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.'''
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito',
         'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20 para saber como escrever por extenso: '))
    if num >= 0 and num <= 20:
        print('Você digitou o número', tupla[num])
        break
    else:
        print('O oreia seca, é pra digitar um número entre 0 e 20, nem maior nem menor que isso...')
        print('Vou te dar mais uma chance...')
