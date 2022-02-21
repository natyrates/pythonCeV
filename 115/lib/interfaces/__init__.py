print('\033[31m====== DESAFIO 115 ======\033[m')
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lst):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lst:
        print(f'\033[95m{cont}\033[m - \033[94m{item}\033[m')
        cont += 1
    print(linha())
    op = leiaInt('\033[92mSua opção: \033[m')
    return op