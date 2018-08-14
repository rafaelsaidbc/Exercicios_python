'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final mostre:
a) qual é o total gasto na compra;
b) quantos produtos custam mais de R$1000,00;
c) qual é o nome do produto mais barato.'''
total = produtos_acima_1000 = preco_mais_barato = contador = 0
# a variavel preco_mais_barato e a variavel contador sao necessárias para definir
# o produto com menos preço
nome_mais_barato = ''
continua = ''
nome = ''
preco = 0
while True:
    print('=' * 30)
    print('Cadastro de produtos')
    print('=' * 30)
    continua = str(input('Quer continuar[S/N]? ').upper().strip())
    if continua == 'S':
        nome = str(input('Qual o nome do produto? '))
        preco = float(input('Qual o preço do produto? R$'))
        contador += 1
        if contador == 1:  # isso quer dizer que se o primeiro produto for o mais barato
            # a variavel preco_mais_barato recebe a variavel preco.
            preco_mais_barato = preco
            nome_mais_barato = nome
        else:
            if preco < preco_mais_barato:  # Se algum próximo produto for mais barato, a variavel preco_mais_barato recebe esse produto
                preco_mais_barato = preco
                nome_mais_barato = nome
        total += preco
        if preco > 1000:
            produtos_acima_1000 += 1
    else:
        break
print(f'Você gastou um total de R${total:.2f}.\n'
      f'Você comprou {produtos_acima_1000} produtos que custam mais de R$1000,00!\n'
      f'O produto mais barato que você comprou foi {nome_mais_barato}, que custou {preco_mais_barato}.')
