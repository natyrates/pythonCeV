print('\033[31m====== DESAFIO 85 ======\033[m')
num = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados: {num[0]}')
print(f'Os valores impares digitados: {num[1]}')