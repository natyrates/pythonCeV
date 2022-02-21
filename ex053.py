print('\033[31m====== DESAFIO 53 ======\033[m')
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inv = ''
for letra in range(len(junto) - 1, -1, -1):
    inv = inv + junto[letra]
print('O inverso de {} é {}'.format(junto, inv))
if inv == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')