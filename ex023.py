num = int(input('Digite um número entre 0 e 9999: '))
unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhar = num // 1000 % 10
print('O número {} tem:\nunidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(num, unidades, dezenas, centenas,
                                                                                  milhar))
print('Outra forma de fazer, só funciona se o número tiver 4 dígitos: ')
numero = input('Digite um numero entre 0 e 9999: ')
print('O número {} tem: \nunidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(numero, numero[3], numero[2],
                                                                                   numero[1], numero[0]))
