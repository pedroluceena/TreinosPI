from math import sqrt , trunc
print('------------JOGO-DA-VIDA--------------')
name = str(input('Qual é o seu nome ?: ')).strip()
print('Muito prazer {} Bem vido ao Jogo da vida , esse jogo tem um fator curioso'.format(name))
idade = int(input('Qual é a sua idade?(Coloque apenas os numero): '))
power = (idade*30)
raiz = sqrt(power)
print('Bom vamos começar  {} ,poxa sua idade é {},se você for uma pessoa mais velha vai se dar bem'.format(name,idade))
print('O seu nivel de poder é {}, o valor dele é o valor da sua idade e multiplicado por 30 Pontos e depois disso usamos um calculo em raiz'.format(trunc(raiz)))
print('Bom vamos começar os Desafios da Vida caso aparece True(Venceu) caso for False(Perdeu)')
print('Se seu poder for maior que 10 Pontos você vencerar o Primeiro Desafio da Vida a Juventude !',(trunc(raiz)>10))
print('Se seu poder for maior que 20 Pontos você vencerar o Segundo Desafio a Responsabilidade !',(trunc(raiz)>20))
print('Se seu poder for maior que 30 Pontos você vencerar o Terceiro Desafio da Maturidade!',(trunc(raiz)>30))
print('Se seu poder for maior que 40 Pontos você vencerar o Quarto Desafio da Sabedoria!',(trunc(raiz)>40))
print('Se seu poder for maior que 50 Pontos você vencerar o Sexto Desafio da Sobrevivência!',(trunc(raiz)>50))
print('.')
print('.')
print('.')
print('.')                                                                                               
print('Muito obrigado por jogar esse game ,se caso você venceu todos os chefes você literalmente se tornou.')