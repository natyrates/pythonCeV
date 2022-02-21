print('\033[31m====== DESAFIO 57 ======\033[m')
sexo = str(input('Digite o sexo da pessoa: [M/F] ')).upper().strip()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Por favor, informa o sexo da pessoa: [M/F] ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
