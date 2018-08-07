n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))
if n1 > n2 > n3:
    print('O menor número é {} e o maior é {}.'.format(n1, n3))
if n2 > n1 > n3:
    print('O menor número é {} e o maior {}'.format(n3, n2))
if n3 > n1 > n2:
    print('O menor número é {} e o maior {}.'.format(n2, n3))
if n1 > n3 > n2:
    print('O menor número é {} e o maior {}.'.format(n2, n1))
if n2 > n3 > n1:
    print('O menor número é {} e o maior {}.'.format(n1, n2))
if n3 > n2 > n1:
    print('O menor número é {} e o maior {}.'.format(n1, n3))
