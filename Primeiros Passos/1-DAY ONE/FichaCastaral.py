#Ficha Cadastral 
print('-----SEJA---BEM---VINDO-----')
print('Essa ficha Cadastral é para o Curso')
nome = str(input('Qual Seu nome?: '))
idade = int(input('Qual é sua idade?: '))
cidade = str(input('Onde você mora?: '))
Bairro = str(input('Em que bairro você mora?: '))
job = str(input('Qual é o seu trabalho?: '))
salário = str(input('Quanto que você ganha por mês?(valor liquído):R$'))
print('----------FICHA-CADASTRAL-----------')
print('Seu nome é {} você tem {}, e você mora na cidade {} e no bairro {} , aparetimente você trabalha com {} e ganha {} (Espero que seja um bom sálario)'.format(nome,idade,cidade,Bairro,job,salário))