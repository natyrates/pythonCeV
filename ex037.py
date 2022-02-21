print('\033[31m====== DESAFIO 36 ======\033[m')
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('\033[36m-' * 16)
print('1 - Binário\n'
      '2 - Octal\n'
      '3 - Hexadecimal')
print('\033[36m-\033[m' * 16)
op = int(input('Sua opção: '))
if op == 1:
    b = bin(num)
    print('O número {} convertido em binário é: {}'.format(num, b[2:]))
elif op == 2:
    o = oct(num)
    print('O número {} convertido em octal é: {}'.format(num, o[2:]))
elif op == 3:
    h = hex(num)
    print('O número {} convertido em hexadecimal é: {}'.format(num, h[2:]))
else:
    print('Opção inválida! Tente novamente.')
