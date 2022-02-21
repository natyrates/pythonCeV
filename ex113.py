print('\033[31m====== DESAFIO 113 ======\033[m')
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


n = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'Você acabou de digitar o número inteiro {n}.')
print(f'Você acabou de digitar o número real {r}.')