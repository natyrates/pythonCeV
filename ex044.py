print('\033[31m====== DESAFIO 44 ======\033[m')
print('\033[32m-' * 20)
print('    LOJAS PYTHON')
print('\033[32m-\033[m' * 20)
preco = float(input('Preço das compras: R$'))
print('\033[35m=+'*15)
print('     FORMAS DE PAGAMENTO\n'
      '1 - à vista dinheiro/cheque\n'
      '2 - à vista cartão\n'
      '3 - 2x no cartão\n'
      '4 - 3x ou mais no cartão')
print('\033[35m=+\033[m'*15)
op = int(input('Qual é a opção? '))
if op == 1:
    des = preco - (preco * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, des))
elif op == 2:
    des = preco - (preco * 0.5)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, des))
    print('')
elif op == 3:
    parc = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parc))
elif op == 4:
    p = int(input('Quantas parcelas? '))
    aum = preco + (preco * 0.20)
    p1 = aum / p
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(p, p1))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, aum))
else:
    print('Opção inválida! Tente novamente.')