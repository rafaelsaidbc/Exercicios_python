import random
from time import sleep

num = random.randint(0, 5)
num_user = int(input('Digite um número entre 0 e 5: '))
print('Processando...')
sleep(5)
if num == num_user:
    print('Parabéns, você advinhou o "pensamento" do computador!')
else:
    print('Vixe, você não advinhou o número do computador. Tente novamente...')
print('O computador sorteou o número {}'.format(num))
