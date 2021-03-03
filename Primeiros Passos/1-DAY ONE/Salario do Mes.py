#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
#Editando a questão para ficar mais desafiadora 
nome = input('Qual é o seu nome?: ')
ganho = float(input('Quanto que você ganha por hora liquída?: '))
mes = float(input('Quanto que você trabalha por mês?(quantando as  horas extras): '))
km = float(input('Quantos KM de distância tem do seu trabalho a sua casa ? '))
gasolina = (0.12 * km)
mesg = gasolina * 25
s = ganho * mes
st = s - gasolina
print('Muito Prazer! {} , vamos aproveitar esse momento e iremos fazer uma breve pesquisa da sua rotina , primeiro observamos aqui que você ganha por hora R$ {} com isso sua media salarial liquida é R$ {} , porém você tem carro e com isso gasta com gasolina,com esses gasto o valor diario é R${} e o gasto total do mês é {} , com isso seu sálario fica sobrando apenas R${}'.format(nome,ganho,s,gasolina,mesg,st))