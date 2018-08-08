'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma das mensagens a seguir:
- média abaixo de 5.0 = reprovado
- média entre 5.0 e 6.9 = recuperação
- média acima de 7.0 = aprovado'''
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média foi {}. Você não se dedicou o suficiente e está REPROVADO!'.format(media))
elif 5.0 < media < 6.9:
    print('Sua média foi {}. Se dedique um pouco mais para a RECUPERAÇÃO!'.format(media))
else:
    print('Parabéns! Com a média {} você está APROVADO'.format(media))
