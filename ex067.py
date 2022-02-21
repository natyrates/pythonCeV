print('\033[31m====== DESAFIO 67 ======\033[m')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        p = n * c
        print(f'{n} x {c:2} = {p}')
print('PROGRAMA DE TABUADA ENCERRADO! Volte sempre.')
