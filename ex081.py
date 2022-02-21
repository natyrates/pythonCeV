print('\033[31m====== DESAFIO 81 ======\033[m')
num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescentes são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
