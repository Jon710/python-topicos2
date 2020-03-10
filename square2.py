import turtle

bob = turtle.Turtle()

def square2(t, l):
	for i in range(4):
		t.fd(l)
		t.lt(90)

leonardo = turtle.Turtle()
donatelo = turtle.Turtle()

square2(leonardo, 200)

donatelo.penup()
donatelo.setpos(60, 30)
donatelo.pendown()

square2(donatelo, 300)

turtle.mainloop()