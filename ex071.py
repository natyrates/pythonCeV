print('\033[31m====== DESAFIO 71 ======\033[m')
print('\033[32m-'*20)
print('     BANCO CEV')
print('\033[32m-\033[m'*20)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totalc = 0
while True:
    if total >= ced: #QUANTAS VEZES TIRA R$50 DO TOTAL
        total -= ced
        totalc += 1
    else:
        if totalc > 0:
            print(f'Total de {totalc} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalc = 0
        if total == 0:
            break
print('\033[32m-\033[m'*45)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
