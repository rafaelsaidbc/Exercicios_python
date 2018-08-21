'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
vitorias = 0
while True:
    escolha = str(input('Você quer par ou ímpar? [P/I]').upper().strip())
    if escolha in 'PI':
        jogador = int(input('Jogue seu número: '))
        computador = randint(0, 10)
        soma = jogador + computador
        if escolha == 'P':
            if soma % 2 == 0:
                print(f'Você jogou {jogador} e o computador {computador}.')
                print(f'A soma foi {soma}. O jogador venceu.')
                vitorias += 1
            else:
                print(f'Você jogou {jogador} e o computador {computador}.')
                print(f'A soma foi {soma}. O computador venceu')
                break
        elif escolha == 'I':
            if soma % 2 != 0:
                print(f'Você jogou {jogador} e o computador {computador}.')
                print(f'A soma foi {soma}. O jogador venceu.')
                vitorias += 1
            else:
                print(f'Você jogou {jogador} e o computador {computador}.')
                print(f'A soma foi {soma}. O computador venceu.')
                break
    else:
        print('Escolha um opção válida.')
print(f'Você venceu {vitorias} vezes.')
