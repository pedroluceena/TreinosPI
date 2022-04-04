nome = input('Qual é o seu nome?: ')
nota1 = float(input('Diga sua primeira nota: '))
nota2 = float(input('Diga sua segunda nota: '))
nota3 = float(input('Diga sua terceira nota: '))
nota4 = float(input('Diga sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4 ) / 4  
if media >= 7:
    print('Parabéns Aluno(a) {} , sua média foi {:.1f} e você foi APROVADO!'.format(nome,media)) 
#elif media >= 5 or media >= 6.9:
#    print('O Aluno {} , sua média foi {:.1f} e você está de RECUPERAÇÃO!'.format(nome,media))
#elif media >= 0 or media >= 4.9:
#    print('O Aluno {} , sua média foi {:.1f} e você foi REPROVADO!'.format(nome,media))

elif 5 < media < 6.9:
    print('O Aluno {} , sua média foi {:.1f} e você está de RECUPERAÇÃO!'.format(nome,media))
elif 4.9 > media > 0:
    print('O Aluno {} , sua média foi {:.1f} e você foi REPROVADO!'.format(nome,media))