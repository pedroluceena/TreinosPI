from random import randint
from time import sleep
print('-+'*20)
computador = randint(0, 5)
jogador = int(input('Pensei num numero de 0 a 5 diga o numero:'))
print('-+'*20)
print('...LOADING....')
sleep(1)
if jogador == computador:
     print('Parabéns você venceu!!!!')
else:
     print('Você perdeu! eu pensei no numero {} e você no {}'.format(computador,jogador))