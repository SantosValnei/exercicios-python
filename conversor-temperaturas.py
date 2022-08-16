#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_celcius = float(input('Informe a temperatura C°: '))
temperatura_fahrenheit = (temperatura_celcius * 9/5) + 32
print('A temperatura de {}°C corresponde a 88.7°F'.format(temperatura_celcius, temperatura_fahrenheit))