from datetime import date
ano = date.today().year
sex =  int(input('Diga qual é o seu Sexo 1 para :[MASCULINO] 2 para :[FEMININO]:'))
if sex == 1:
    print('O alistamento é obrigatório para Você!')
elif sex == 2:
    print('O alistamenton não é obrigatório para você!')
nasc =  int (input('Qual é o ano de nascimento: '))
idade = ano - nasc
print('Quem nasceu em {} tem {} anos {}.'.format(nasc, idade,ano))
if idade == 18:
    print('Você tem que alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 , ainda falta {} anos para o alistamento'.format(saldo))
    falta = ano + saldo
    print('Seu alistamento será em {}'.format(falta))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ser alistado há {} anos'.format(saldo))
    falta = ano - saldo
    print('Seu alistamento foi em {}'.format(falta))
    print('Você teria {} anos no Exercio , já seria um Sargento ou Capitão!'.format(saldo))
