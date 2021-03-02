peixe = float(input('Qual foi a quantidade em KG de peixe que ele trouxe(LEMBRE-SE QUE ACIMA DE 50KG paga multa!): '))
if peixe < 51:
    print('Você não pagarar a multa, esse quantidade foi aprovada ')
else:
    peixe > 50
    multa = ((peixe-50)*4)
    print('Você irar pagar a multa ,e será {}'.format(multa))