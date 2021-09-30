#!/usr/bin/env python3
s = str(input("s: "))
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
n4 = int(input("n4: "))

import sys
s = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]

isinstance(s, str)
isinstance(n1, int)
isinstance(n2, int)
isinstance(n3, int)
isinstance(n4, int)

if len(s) < n4:
print('n4 tem que ser menor que o comprimento da sequencia')
elif len(s) < n3:
print('n3 tem que ser menor que o comprimento da sequencia')
elif len(s) < n2:
print('n2 tem que ser menor que o comprimento da sequencia')
elif len(s) < n1:
print('n1 tem que ser menor que o comprimento da sequencia')
else:
print('Os dados foram informados da maneira correta, checkpoint reached!')

CDS1 = s[n1:n2]
print('CDS1 contem os codons', CDS1)
inicio = CDS1[0:3]
'ATG' in inicio

CDS2 = s[n3:n4]
print('CDS2 contem os codons', CDS2)
final = CDS2[-3:]

if 'TAG' in final and 'ATG' in inicio:
print(CDS1 + CDS2)
elif 'TGA' in final and 'ATG' in inicio:
print(CDS1 + CDS2)
elif 'TAA' in final and 'ATG' in inicio:
print(CDS1 + CDS2)
else:
print('A sequencia de cDNA fornecida nao possui codons de inicio ou parada')















