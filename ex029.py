print('====== DESAFIO 29 ======')
v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('Ultrapassou a velocidade de 80km. Você será multado.')
    m = 7 * (v - 80)
    print('Valor da multa: R${:.2f}'.format(m))
else:
    print('Você está no limite certo de velocidade. Parabéns!')