import math

x = 3
y = 5

s = 'Joao'

print('{} + {} = {} '.format(x, y, x + y))

print('O {} eh palmeirense '.format(s))

print('Pi = {:11.8f}'.format(math.pi))

for i in range(len(s)):
	print('s[{}] = \'{}\ '.format(i, s[i]))