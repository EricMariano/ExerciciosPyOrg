#6.Faça um Programa que leia três números e mostre o maior deles.
def isnumber(n1):

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

def isnumber(n3):

    try:
        float(n3)
        return True
    except:
        return False    

while True:
    n1 = input('Digite um número:')

    if isnumber(n1):
        n1 = float(n1)
    else:
        print('Erro!(1ºnum) digite um número. Reiniciando...')
        continue
    n2 = input('Digite outro número: ')

    if isnumber(n2):
        n2 = float(n2)
    else:
        print('Erro!(2ºnum) digite um número. Reiniciando...')
        continue

    n3 = input('Digite mais um número: ')

    if isnumber(n3):
        n3 = float(n3)
    else:
        print('Erro!(3ºnum) digite um número. Reiniciando...')
        continue

    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)

    print(f'O maior número foi {maior} e o menor foi {menor}.')
    break