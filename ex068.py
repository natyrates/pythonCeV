print('\033[31m====== DESAFIO 68 ======\033[m')
import random
print('\033[36m-'*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('\033[36m-\033[m'*25)
cont = 0
while True:
    comp1 = random.randint(1,10)
    lista = ['P', 'I']
    comp2 = random.choice(lista)
    jog1 = int(input('Diga um valor: '))
    jog2 = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jog1} e o computador {comp1}.')
    soma = comp1 + jog1
    if soma % 2 == 0:
        print(f'Total de {soma}. DEU PAR!')
        if jog2 == 'P':
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Total de {soma}. DEU ÍMPAR!')
        if jog2 == 'I':
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('-' * 30)
print(f'GAMER OVER! Você venceu {cont} vezes.')