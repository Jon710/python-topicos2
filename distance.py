import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.sqrt(dx ** 2 + dy ** 2)

print('Teste')
print(distance(0, 1, 3, 5))

