casa = float(input('Qual é o valor da Casa?:R$'))
Renda = float(input('Quanto de renda você tem?:R$'))
anos = int(input('Quantos anos de financimento?:'))
prestação = casa / (anos * 12)
minimo =(Renda * 0.3)
print('Para pagar  a casa {:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa,anos,prestação))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO')