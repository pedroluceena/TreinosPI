nome = str(input('Qual é o seu nome ?:'))
if nome =='Pedro' or nome =='Lucas' or nome =='Miguel':
    print('Que nome bonito você tem !')
elif nome =='Matheus' or nome =='Maria' or nome =='Jose' or nome =='Ana' or nome =='Antonio' or nome =='Jessica' or nome =='Francisco' or nome =='Paulo':
    print('Seu nome é bastante popular no Brasil.')
elif nome =='Paulo' or nome =='Juliana' or nome =='Marcia' or nome =='Fernanda' or nome =='Camila':
    print('Seu nome é forte no Brasil')
else:
    print('Seu nome é normal')
print('Tenha um Bom dia ,{}!'.format(nome))