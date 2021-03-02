print('AUMENTO DE SALARIO')
salario=float(input('Qual é o valor do salario:R$'))
acrescimo=salario*0.15
s=salario+acrescimo
print('Parabéns o seu salario é R${} ,teve um aumento de 15% com isso ficou R${:.2f} reais'.format(salario,s))