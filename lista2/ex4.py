#4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
while True:
    letra = input('Digite uma letra: ').capitalize()

    if letra.isdigit():
        print('Digite uma letra, não um número.')
        continue   
    else:
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            print(f'A letra {letra} é uma vogal.')
            break
        else:
            print(f'A letra {letra} é uma consoante.')
            break
