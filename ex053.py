'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
texto = str(input('Digite uma frase para saber se ela é um palíndromo: ')).strip().upper()
palavras = texto.split()
texto_junto = ''.join(palavras)
print('O texto que você digitou foi {}'.format(texto_junto))
texto_invertido = ''
for letra in range(len(texto_junto) - 1, -1, -1):
    texto_invertido += texto_junto[letra]
print('O texto invertido fica {}.'.format(texto_invertido))
if texto_junto == texto_invertido:
    print('Você digitou um palíndromo.')
else:
    print('Você NÃO digitou um palíndromo.')
