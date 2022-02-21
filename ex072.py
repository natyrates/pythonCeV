print('\033[31m====== DESAFIO 72 ======\033[m')
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenone', 'vinte')
while True:
    op = int(input('Digite um número entre 0 e 20: '))
    if 0 <= op <= 20:
        break
    print('Tente novamente. ',end='')
print(f'Você digitou o número {numeros[op]}.')