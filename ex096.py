'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno (largura e comprimento) e mostre a área do terreno.
'''


def area(*num):
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    area = largura * comprimento
    print(f'A área do terreno {largura} x {comprimento} é de {area}m².')


area()
