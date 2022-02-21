print('\033[31m====== DESAFIO 87 ======\033[m')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatot = somater= maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
print('-'* 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somatot += matriz[l][c]
    print()
print('-'* 40)
print(f'A soma dos valores pares é: {somatot}.')
for l in range(0, 3):
    somater += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somater}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')

