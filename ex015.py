km = float(input('Quantos km você percorreu? '))
dias = float(input('Você ficou com o carro quantos dias? '))
pagamento = (60 * dias)+(km * 0.15)
print('Você pagará um total de R${} reais por {} km e {} dias de aluguel.'.format(pagamento, km, dias))