print('\033[31m====== DESAFIO 78 ======\033[m')
num = list()
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'Você digitou os valores: {num}')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor encontado foi {menor} nas posições ',end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}... ', end='')
print()