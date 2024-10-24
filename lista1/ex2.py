#4
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))

media1 = (n1 + n2) / 2
media2 = (n3 + n4) / 2
mediageral = (n1 + n2 + n3 + n4) / 4

print(f'Sua média do primeiro semestre foi {media1:.1f} 
      e a sua média do segundo semestre foi {media2:.1f} 
      e sua média geral foi {mediageral:.1f}')