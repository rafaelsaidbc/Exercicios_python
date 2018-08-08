'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a
condição de pagamento:
- à vista no dinheiro/cheque: 10% de desconto
- à vista no cartão: 5%  de desconto
- até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
preco = float(input('Digite o preço do produto: '))
pagamento = int(input('Selecione a forma de pagamento dentre as opções: '
                      '\n[1] À vista no dinheiro ou cheque'
                      '\n[2] À vista no cartão'
                      '\n[3] Até 2x no cartão'
                      '\n[4] 3x ou mais no cartão\n'))
if pagamento == 1:
    print('O produto terá um preço final de R${:.2f}.'.format(preco - (preco * 0.10)))
elif pagamento == 2:
    print('O produto terá um preço final de R${:.2f}.'.format(preco - (preco * 0.05)))
elif pagamento == 3:
    print('O produto terá um preço final de R${:.2f}, e cada parcela será R${:.2f}'.format(preco, (preco / 2)))
elif pagamento == 4:
    vezes = int(input('Em quantas vezes você deseja dividir? '))
    preco_final = preco + (preco * 0.20)
    print('O produto terá um preço final de R${:.2f}, e cada parcela será R${:.2f}.'.format(preco_final,
                                                                                            (preco_final / vezes)))
else:
    print('Você não selecionou um opção válida.')
