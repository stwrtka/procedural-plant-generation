import turtle

#functions need
#l-system (might output a string)
#smth to interpert string from the l-system and calls the draw function

#things that SQL can effect direction(if it goes forward, left, right), lenght(?) colour, size of leaf(?)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.home()

plant = 'FFFF-FFF-F-F+FFF-F-FFF'
#grammer 
#axiom

#[] -->start and end of the branch
angle = 90

def l_system(): #going to create a string 
    for type in plant:
        draw_plant(type, angle)

#any time you see a certain letter it should be this thing instead; F -> FF+F-[+-F]

def draw_plant(type, angle):
    if type == 'F': #forward
        turtle.forward(20)
    elif type == '-': #left
        turtle.left(angle)
    elif type == '+': #right
        turtle.right(angle)
    elif type == 'L': #leaf
        turtle.showturtle()
        turtle.stamp()
        turtle.hideturtle()

l_system()

turtle.getscreen()._root.mainloop()