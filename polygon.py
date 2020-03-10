import turtle

bob = turtle.Turtle()

def polygon(t, l, n): # t eh turtle, l eh length, n eh sides
	
	angulo = 360 / n

	for i in range(n):
		t.fd(l)
		t.lt(angulo)

	turtle.mainloop()

polygon(bob, 100, 5)


