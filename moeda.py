def aumentar(num, por, formt=False):
    a = num + (num * por/100)
    return a if formt is False else moeda(a)

def diminuir(num, por, formt=False):
    dim = num - (num * por/100)
    return dim if formt is False else moeda(dim)

def dobro(num, formt=False):
    d = num * 2
    return d if formt is False else moeda(d)

def metade(num, formt=False):
    m = num / 2
    return m if formt is False else moeda(m)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num, pora=10, pord=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'A metade do preço: \t{metade(num, True)}')
    print(f'O dobro do preço: \t{dobro(num, True)}')
    print(f'Aumentando {pora}%: \t{aumentar(num, 10, True)}')
    print(f'Diminuindo {pord}%: \t\t{diminuir(num, 13, True)}')
    print('-' * 30)