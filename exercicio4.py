# 4. Leia as descrições das funções do módulo turtle (https://docs.python.org/3/library/turtle.html) e,
# usando sua enorme criatividade, crie um programa que faça algo interessante.
# Explique o seu programa. (2,5 pontos)

# programa que desenha a estrela do Mundial de 51
# do Palmeiras.

import turtle

# Instanciando objetos da classe Turtle e Screen
screen = turtle.Screen()
porco = turtle.Turtle()

screen.setup(800, 600)  # tamanho da tela
screen.bgcolor('black')  # cor do fundo da tela
cores = ['white', 'green', 'green', 'green', 'white']
porco.pensize(6)
porco.penup()
porco.setpos(-90, 30)  # posição que a estrela começa
porco.pendown()
for i in range(5):  # cada aresta da estrela será desenhada nesse for
    porco.pencolor(cores[i])
    porco.forward(200)
    porco.right(144)
porco.penup()
# posiçao onde será escrito o texto, ao terminar de desenhar a estrela
porco.setpos(-160, -140)
porco.pendown()
porco.pencolor('green')

porco.write('S. E. Palmeiras - Campeão Mundial 51',
            font=("Verdana", 20, "bold"))
porco.ht()  # funcao hide turtle

turtle.mainloop()
