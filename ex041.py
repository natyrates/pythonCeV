print('\033[31m====== DESAFIO 41 ======\033[m')
idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JÚNOR.')
elif idade <=25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
