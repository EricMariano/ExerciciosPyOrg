#2 Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
n3 = float(input('Enter a third number: '))

def decreaseOrder():
    numbersList = [n1, n2, n3]
    numbersList.sort(reverse=True)
    print(numbersList)

decreaseOrder()