#4. Faça um programa para a leitura de duas notas parciais de um aluno. 
def is_number(n1):

    try:
        float(n1)
        return True
    except:
        return False

def isnumber(n2):

    try:
        float(n2)
        return True
    except:
        return False   

def codigo():

    while True:
        n1 = input('Informe sua nota da 1º unidade: ')
        n1 = n1.replace(',','.')
        
        if is_number(n1):
            n1 = float(n1)
        else:
            print('Digite um número. Reiniciando...')
            continue

        n2 = input('Informe sua nota da 2º unidade: ')
        n2 = n2.replace(',','.')
        
        if isnumber(n2):
            n2 = float(n2)
        
        soma = n1 + n2
        
        media = soma / 2

        if media == 10:
            print(f'Aprovado com distinção, sua média foi {media:.1f}. Parabéns!')
            break
        elif media >= 7:
            print(f'Aprovado, sua média foi {media:.1f}. Parabéns!')
            break
        elif media < 7:
            print(f'Reprovado, sua média foi {media:.1f}. Melhore.')
            break
        else:
            print('Digite um número. Reiniciando...')
            continue

codigo()