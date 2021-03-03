a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Testanto quem é o maior 
menor = a 
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c 
#Testanto quem é o Maior 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))