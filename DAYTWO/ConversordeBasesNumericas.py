number = int(input('Digite um numéro inteiro: '))
print('''Escolha um das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Coverter para HEXADECIMAL''')
option = int(input('Sua opção: '))
if option == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number,bin(number)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number,oct(number)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number,hex(number)[2:]))
else:
    print('Você não escolhou nem uma opção')