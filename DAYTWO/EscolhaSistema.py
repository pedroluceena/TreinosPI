sistema = str(input('Qual sistema operacional você usa ? Linux/Windows/MacOs?(Escolha uma das três),caso for linux coloque a distro certa:'))
if sistema =='Windows':
    print('Você usa o sitema operacional mais usado MUNDO!')
elif sistema =='Kali' or sistema =='Red Hat':
    print('Você é Hacker em!')
elif sistema =='Ubuntu' or sistema =='Kubuntu' or sistema =='Lubuntu' or sistema =='Debian':
    print('Esse sitema linux é comum.')
elif sistema =='MacOs':
    print('Poxa que bacana!!! 10% da população que usa pc/notebook usa MacOs e você faz parte delas.')
else:
    print('Esse sistema é bem underground.....')