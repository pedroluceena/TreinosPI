km = float(input('A velocidade do carro em KM/H:'))
multa = (km-80)*7
if km > 80:
    print('Você foi multado, o valor a ser pago é R$ {}, DIRIJA COM CUIDADO'.format(multa))
else:
    print('Tenha um Bom Dia!Dirija com Segurança!')
    
