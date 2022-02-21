print('\033[31m====== DESAFIO 43 ======\033[m')
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / (pow(altura, 2))
print('Com IMC igual a {:.1f}, você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('no seu peso ideal.')
elif 25 <= imc < 30:
    print('em sobrepeso.')
elif 30 <= imc < 40:
    print('obeso.')
else:
    print('com obesidade mórbida, cuidado.')
