'''Faça um programa que leio o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
masculino = 'M'
feminino = 'F'
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa, [F] para feminino ou [M] para masculino: ').upper())
    if sexo != 'M' and sexo != 'F':
        print('Digite certo, presta atenção no serviço...')
feminino = 'F'
masculino = 'M'
if sexo == 'M':
    print('A pessoa é do sexo masculino.')
else:
    print('A pessoa é do sexo feminino.')
