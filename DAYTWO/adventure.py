"""
Bom esse código foi feito para treinos com If , Elif e Else, criei uma interação com o usuario bem simples 
Para que ele possa brincar
Possui apenas um chefe e quero colocar barreiras para ver se o usuario consegue passar das etapas 
alpha 0.0.1 

"""
print('Seja bem vido ao meu Mundo!')
#Para que o Usuario seja bem recebido , sempre pergunto o nome
nome = input('Nome do Herói:')
print('Seja bem-vindo {} ! Aqui começamos a aventura, primeiramente vamos fazer uma distribuição de poder.'.format(nome))
#Criei tem habilidades para dar um ar de brincadeira mais elaborada

print(" Você possui apenas 100 para distribuir para suas habilidades.")
print(" [FORÇA] [MÁGIA] [INTELIGÊNCIA] ")
print("Dica:Tente deixar os pontos bem distribuidos não foque em uma habilidade só.")
pontos = 100
forca = int(input("Digite o valor da sua força:"))
mana = int(input("Digite o valor da sua Magia:"))
inte = int(input("Digite o valor da sua Inteligencia:"))
total = (forca + mana + inte)
#Aqui é uma parte legal , coloquei um limite de pontos para que o usuário não passe dele, ou deixe de colocar.
if total == pontos:
    print("ótimo você distribuiu bem os pontos!")
else:
    print("Refaça! Você distribuiu mal os pontos ou colocou a mais!")
    print("Ótimo agora vamos conferir os valores são Força: {} , Mágia {} , inteligência {}.".format(forca, mana, inte))

print("Agora vamos fazer um teste de inteligencia para ver que nivel você ficou!")
if inte >= 50:
     print("Você é muito inteligente um genio talvez.")
elif inte >= 30:
     print("Você tem a inteligência legal.")
elif inte >= 10:
    print("Você tem a inteligência básica.")
else:
    print("Você nao tem a inteligência")

print("Agora vamos fazer um teste de força para ver que nivel você ficou!")
if forca >=50:
    print("Você é muito forte,Berserk!")
elif forca >= 30:
    print("Você tem uma força legal!")
elif forca >= 10:
    print("Você é fraco lhe falta ódio by:Itachi")
else:
    print("Você é muito fraco !!!!")
   
print("Agora vamos fazer um teste de Mágia para ver que nivel você ficou!")
if mana >= 50:
    print("Você é o mago SUPREMO!")
elif mana >= 30:
    print("Você tem boa noção da mágia.")
elif mana >= 10:
    print("Sem noção de mágia, mágia para que né ?")
else:
    print("Um cético")

print("Vamos começar!")
#Referência do meu jogo favorito :
print("---------As Aventuras de {}----------".format(nome))
#Esse treinamento e para o jogador entender o básico da aventura 
print("Primeiro vamos para o treinamento, isso é imporante porque vamos ter alguns chefes e eles são complicados")
mestre = 80
forcat = 30
manat = 40
intet = 10
print("A aventura começa com a relação de pontos do jogador e com o oponente, exemplo: se o jogar possui 50 pontos de força e oponente 20,jogador venceu,para o jogador vencer o oponente ele deve ganhar em 2 Habilidades. ")
#Aqui eu usei um sistema como fosse 3vs3 Quem ganha em mais ponto de habilidade vence.
print("Força do Mestre vs Força do {}".format(nome))
if forca > forcat:
    print("Você venceu")
else:
    print("Você perdeu")
print("Mágia do Mestre vs Força do {}".format(nome))
if mana > manat:
    print("Você venceu")
else:
    print("Inteligência do Mestre vs Força do {}".format(nome))
    print("Você perdeu")
if inte > intet:
    print("Você venceu")
else:
    print("Você perdeu")
print("Se você venceu mais de uma vez voce venceu")
print("Agora vamos para o primeiro chefe!")
Dark = 110
forcad = 50
manad = 30
inted = 20
print("Força do Dark vs Força do(a) {}".format(nome))
if forca > forcad:
    print("Você venceu")
else:
    print("Você perdeu")
    print("Mágia do Dark vs Mágia do(a) {}".format(nome))
    if mana > manad:
        print("Você venceu")
    else:
        print("Você perdeu")
    print("Inteligência do Dark vs Inteligência do(a) {}".format(nome))
    if inte > inted:
        print("Você venceu")
    else:
        print("Você perdeu")
print("Se você venceu mais de uma vez voce venceu")

