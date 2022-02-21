print('====== DESAFIO 12 ======')
p = float(input('Digite o preço do produto: R$'))
desc = p - (p * 5/100)
print('Preço com 5% de desconto: R${:.2f}'.format(desc))
