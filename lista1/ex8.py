#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = float(input('Informe a temperatura em grau Celsius: '))
fah = (c * 1.8) + 32

print(f'A temperatura em graus Fahrenheit é de {fah:.1f}')