n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma é {}, \n  produto é {}\n  e a divisão é {:.2f}'.format(s,m,d), end=' ')
print('a divisão inteira é {} e a potencia {}'.format(di,e))