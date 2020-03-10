def right_justify(s):
	tam = len(s)
	print(tam)
	fim = 70 - tam
	print(fim)
	nome = (' '*fim) + s
	print(nome)

right_justify('palmeiras')