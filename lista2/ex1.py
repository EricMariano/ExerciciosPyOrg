#1 Faça um programa que pergunte o preço de três produtos e 
# informe qual produto mais barato.
print('Cheap product')
product1 = float(input('Enter the price of first product: '))
product2 = float(input('Enter the price of second product: '))
product3 = float(input('Enter the price of third product: '))

def checkCheapestProduct():
    productsList = [product1, product2, product3]
    productsList.sort()
    print(f'The cheapest product costs: {productsList[0]}')

checkCheapestProduct()