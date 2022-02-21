print('====== DESAFIO 18 ======')
import math
a = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Analizando o ângulo {:.0f}... \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(a,s,c,t))
