#3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
    sexo = input('Informe seu sexo: (M ou F)')

    try:
        sexo = str(sexo).casefold
    except:
        ...

    if sexo == 'f':
        print('Feminino!')
        break
    elif sexo == 'm':
        print('Masculino!')
        break
    else:
        print('Resposta inválida. Faça novamente.')
        continue


