print('\033[31m====== DESAFIO 62 ======\033[m')
print('\033[32m=' * 25)
print('      GERADOR DE PA')
print('\033[32m=\033[m' * 25)
p = int(input('Primeiro termo: '))
r = int(input('Rezão: '))
termo = p
cont = 1
total = 0
x = 10
while x != 0:
    total = total + x
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    x = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
