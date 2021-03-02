Dis = float(input('Qual é a distância da sua viagem?: '))
print('Você está prestes a começar uma viagem de {}KM'.format(Dis))
if Dis <= 200:
    price = Dis*0.50
else:
    price = Dis*0.45
print('É o preço da sua passagem será de R${:.2f}'.format(price))









'''km = float(input('Qual é a distância da viagem?:'))
if km <= 200:
    p1 = (0.5*km)
    print('Sua viagem é {}KM .Você pagarar R${} por essa viagem.'.format(km,p1))
 else:
     p2 = km * 0,45
     print('Sua viagem de {}KM , recebeu um desconto ficar por R${}.'.format(km,p2))'''

     