'''catetoo = float(input('Comprimento do cateto oposto: '))
catetoad = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catetoo ** 2 + catetoad ** 2) ** (1/2)
print('A soma o valor da hipotenusa é {:.2f}'.format(hipotenusa))'''
import math 
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))