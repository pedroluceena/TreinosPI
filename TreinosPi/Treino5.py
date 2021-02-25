print('=========== BOLETIM ==========')
nome=(input('Digite o nome do aluno: '))
n1=float(input('Primeira Nota do Aluno: '))
n2=float(input('Segunda Nota do Aluno: '))
s=(n1+n2)/2
print('O Aluno {} a sua primeira nota foi {:.1f} a seu segunda foi {:.1f} sendo assim sua média é {:.1f} , se for maior 7 passou se for menor 7 reprovou '.format(nome,n1,n2,s))