print('====== DESAFIO 22 ======')
nome = str(input('Digite o nome completo: ')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
espaco = len(nome) - nome.count(' ')
primeiro = nome.find(' ')
print('Maíuscula: {}\nMinúscula: {}\nNúmero de letras sem espaço: {}\nPrimeiro nome tem: {} letras'.format(maiuscula,minuscula,espaco,primeiro))
