print('-+' * 20)
print('Anlisador de Triângulos')
print('-+' * 20)
r1 = float(input('Primeiro Segmento:')) 
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')



