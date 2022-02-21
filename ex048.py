print('\033[31m====== DESAFIO 48 ======\033[m')
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print('Somatório dos {} valores: {}'.format(cont, s))