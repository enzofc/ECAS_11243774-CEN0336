#!/usr/bin/env python3
print('Insira os lados do triangulo')
a = int(input("a: "))
b = int(input("b: "))
import sys
a = sys.argv[1] # obter primeiro cateto
b = sys.argv[2] # obter segundo cateto
isinstance(a, int) # confirmar que o valor inserido e um inteiro
isinstance(b, int) # confirmar que o valor inserido e um inteiro
if a < 1000 and b < 1000: # se os numeros inseridos forem corretos
print('O quadrado da hipotenusa para o triangulo retângulo com lados a=X e b=Y,e', a^2 * b^2) # determinacao da hipotenusa
elif a >= 1000 and b < 1000: # caso apenas o segundo lado seja menor que 1000
print('O primeiro lado deve ser menor que 1000')
elif a < 1000 and b >= 1000: # caso apenas primeiro lado seja menor que 1000
print('O segundo lado deve ser menor que 1000')
else a < 1000 and b < 1000: # caso ambos os lados sejam menores que 1000
print('Ambos os lados devem ser menores que 1000')






