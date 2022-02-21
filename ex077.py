print('\033[31m====== DESAFIO 77 ======\033[m')
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')