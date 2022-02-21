print('====== DESAFIO 27 ======')
nome = str(input('Digite o nome completo: '))
d = nome.split()
print('Nome completo: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nome, d[0], d[len(d)-1]))