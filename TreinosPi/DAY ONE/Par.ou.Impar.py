n = int(input('Me diga um numero qualquer: '))
r = n % 2
if r == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR'.format(n))