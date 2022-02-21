print('\033[31m====== DESAFIO 42 ======\033[m')
print('\033[32m-' * 30)
print('Analisador de triângulos...')
print('\033[32m-\033[m' * 30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a != b != c != a:
        print('ESCANELO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')