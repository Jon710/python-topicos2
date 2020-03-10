import turtle

bob = turtle.Turtle()

def square(t):
	for i in range(4):
		t.fd(100)
		t.lt(90)

leonardo = turtle.Turtle()
donatelo = turtle.Turtle()

square(leonardo)

donatelo.penup()
donatelo.setpos(60, 30)
donatelo.pendown()

square(donatelo)

turtle.mainloop()