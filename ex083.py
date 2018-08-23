'''Crie um programa que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
expressao = str(input('Digite uma expressão matemática: '))
lista = []
for caractere in expressao:
    if caractere == '(':
        lista.append(caractere)
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(caractere)
            break
if len(lista) == 0:
    print('Sua expressão é válida.')
else:
    print('Verifique sua expressão, ela não é valida.')
