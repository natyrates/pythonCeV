print('\033[31m====== DESAFIO 82 ======\033[m')
num = list()
pares = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for c, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'A lista completa: {num}')
print(f'A lista de pares: {pares}')
print(f'A lista de impares: {impar}')