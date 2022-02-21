print('====== DESAFIO 31 ======')
d = float(input('Digite a distância da sua viagem: '))
print('A distância da sua viagem é de {}km'.format(d))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('Você irá pagar R${:.2f}'.format(p))