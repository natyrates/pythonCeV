print('\033[31m====== DESAFIO 112 ======\033[m')
from utilidadescev import moeda
from utilidadescev import dado
preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)