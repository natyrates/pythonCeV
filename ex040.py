print('\033[31m====== DESAFIO 40 ======\033[m')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}.'.format(n1, n2, media))
if media < 5:
    print('O aluno está REPROVADO!')
elif media >= 5 and media < 7:
    print('O aluno está de RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está APROVADO!')