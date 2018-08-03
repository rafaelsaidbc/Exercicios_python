preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco * 0.05)
print('O preço do produto sem desconto é R${} reais, com desconto de 5% sai por R${:.2f} reais.'.format(preco, desconto))
