print('\033[31m====== DESAFIO 35 ======\033[m')
vc = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu sálario? R$'))
a = int(input('Em quantos anos você irá pagar a casa? '))
p = vc / (a * 12)
if p > s / 0.30:
    print('Negado! Você não pode fazer emprestimo.')
else:
    print('Aprovado! Você irá pagar R${:.2f} em {} anos'.format(p, a))