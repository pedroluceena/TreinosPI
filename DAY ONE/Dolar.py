print('Quanto tem na minha carteira e com esse valor quantos dolares eu posso comprar ?')
n=float(input('Digite o valor:R$'))
s=n/5.41
print('A quantidade que está na minha carteira é R${} e a quantidade que eu posso comprar é US${:.3}'.format(n,s))