num = int(input('Digite um número entre 0 e 9999: '))
unidades = num % 10
resto_unidade = num // 10
dezenas = resto_unidade % 10
resto_dezena = num // 100
centenas = resto_dezena % 10
resto_centenas = num // 1000
milhar = resto_centenas % 10
print('O número {} tem:\nunidade: {}\ncentena: {}\ndezena: {}\nmilhar: {}'.format(num, unidades, dezenas, centenas,
                                                                                  milhar))
print('Outra forma de fazer: ')
numero = input('Digite um numero entre 0 e 9999: ')
div = ' '.join(numero)
dividido = div.split()
print('O número {} tem: \nunidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(numero, dividido[3], dividido[2],
                                                                                   dividido[1], dividido[0]))
