nome = str(input('Qual é o nome ?')).strip()
primeiro = nome.split()
print('Analisando o seu nome...')
print('O seu nome em Maiúscula é:',nome.upper())
print('O seu nome em Minúsculas é: ',nome.lower())
print('A quantidade de caracterios é: ',len(nome)-nome.count(' '))
print('A quantidade de Letras do primeiro é nome é : ',(len(primeiro[0])),'Letras')

#nome = str(input('Digite seu nome completo: ')).strip()
#print('Analisando  seu nome....')
#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))