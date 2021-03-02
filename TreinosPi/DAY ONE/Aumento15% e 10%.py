salario = float(input('Qual é o valor do seu salário?: '))
if salario <= 1250:
    ag = salario + (salario * 0.15)
    print('Seu Salario agora é R${} '.format(ag))
else:
    ai = salario + (salario * 0.10)
    print('Seu Salario agora é R${}'.format(ai))


