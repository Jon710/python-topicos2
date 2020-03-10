def countdown(n):
	if n == 0:
		print("Explode fdp")
	else:
		print(n, end = " ")
		countdown(n-1)

countdown(5)