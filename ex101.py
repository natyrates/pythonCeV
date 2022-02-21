print('\033[31m====== DESAFIO 101 ======\033[m')
from datetime import date
def voto(ano):
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        frase = 'VOTO NEGADO.'
    elif idade >= 16 and idade < 18 or idade > 65:
        frase = 'VOTO OPCIONAL.'
    else:
        frase = 'VOTO OBRIGATÓRIO.'
    return frase

nasc = voto(int(input('Ano de nascimento: ')))
print(nasc)
