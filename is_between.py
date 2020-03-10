def is_between(x, y, z):
	if(y >= x and y <= z):
		return True
	else:
		return False

def is_between2(x, y, z):
	return x <= y <= z

print('Teste is_between')
print(is_between(1, 2, 3))

print('Teste is_between2')
print(is_between2(1, 2, 0))