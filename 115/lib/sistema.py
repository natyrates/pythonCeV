from ex115.lib.interfaces import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArq(arq)
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! por favor, digite uma opação válida.\033[m')
    sleep(1)
