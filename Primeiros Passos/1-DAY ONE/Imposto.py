#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê
print('+-'*10)
print('DESCONTO DE SALÁRIO')
print('+-'*10)
n1 = float(input('Olá! poderia dizer quanto que você ganha por mês?:'))
sl = print('+ Salário Bruto: R$',(n1))
re = (n1*0.11)
inss = (n1*8/100)
si = (n1*5/100) 
v = (re + inss + si)
print('- Sindicato ( 5%) : R${}'.format(si))
print('- INSS (8%) : R${}'.format(inss))
print('- IR (11%): R${}'.format(re))
print('= Salário Liquido : R${}'.format(n1 - v))
