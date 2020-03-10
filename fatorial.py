def fatorial_nao_recursivo(n):
	if n < 0 or not isinstance(n, int):
		return None
	fat = 1
	for i in range(n):
		fat = fat * (i + 1)
	return fat

def fatorial_recursivo(n):
	if n < 0 or not isinstance(n, int):
		return None
	if n == 0 or n == 1:
		return 1
	else:
		return n * fatorial_recursivo(n - 1)

for n in range(10):
	print(fatorial_nao_recursivo(n - 2), fatorial_recursivo(n - 2))


print(fatorial_recursivo(1.5))