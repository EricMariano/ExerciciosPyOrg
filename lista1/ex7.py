#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

fah = float(input('Informe a temperatura graus em Fahrenheit: '))
c =  5 * ((fah-32) / 9)

print(f'A temperatura em graus Celsius é de {c:.1f}')