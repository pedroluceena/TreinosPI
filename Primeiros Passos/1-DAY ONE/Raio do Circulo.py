#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
raio = float(input('Qual é o raio do circulo: '))
area = (math.pi * raio**2)
print('A área do circulo é {:.2f}'.format(area))