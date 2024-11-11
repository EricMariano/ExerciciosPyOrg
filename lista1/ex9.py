# 9.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. (C * 9/5) + 32 = F
# And Fahrenheit to Celsius, asking for the user what converter his want. C = 5 * ((F-32) / 9).

converterPick = input('Whats converter you wants 1°(C to F), 2°(F TO C), 3°(Both): ')

if converterPick == '1°' or converterPick == '1' or converterPick == 'first' or converterPick == 'primeiro' or converterPick == 'C to F':
    print('°Celsius to °Fahrenheit Converter!')
    tempC = float(input('Enter a temperature in °Celsius: '))
    tempF = (tempC * 9/5) + 32
    print(f'{tempC}°C in degree Fahrenheit is {tempF:.1f}°F')

elif converterPick == '2°' or converterPick == '2' or converterPick == 'second' or converterPick == 'segundo' or  converterPick == 'F to C':
    print('°Fahrenheit to °Celsius Converter!')
    tempF = float(input('Enter a temperature in °Fahrenheit: '))
    tempC = 5 *((tempF - 32) / 9)
    print(f'{tempF}°F in degree Celsius is {tempC:.1f}°C')

else:
    print('°Celsius to °Fahrenheit Converter!')
    tempC = float(input('Enter a temperature in °Celsius: '))
    tempF = (tempC * 9/5) + 32
    print(f'{tempC}°C in degree Fahrenheit is {tempF:.1f}°F \n')
    
    print('°Fahrenheit to °Celsius Converter!')
    tempF = float(input('Enter a temperature in °Fahrenheit: '))
    tempC = 5 *((tempF - 32) / 9)
    print(f'{tempF}°F in degree Celsius is {tempC:.1f}°C')
    