print('\033[31m====== DESAFIO 66 ======\033[m')
cont = 0
soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} números deu {soma}.')
