import turtle

#functions need
#l-system (might output a string)
#smth to interpert string from the l-system and calls the draw function

#things that SQL can effect direction(if it goes forward, left, right), lenght(?) colour, size of leaf(?)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.home()

plant = 'F-F-L-F-F--LF-F-F-F-L-F-F-F-F-F-F-F-F-F-F-L-F-F-F-F-F-F-F-F-F-F-F-'
def l_system(): #going to creat a string 
    for type in plant:
        draw_plant(type)

def draw_plant(type):
    if type == 'F': #forward
        turtle.forward(100)
    elif type == '-': #left
        turtle.left(100)
    elif type == '+': #right
        turtle.right(100)
    elif type == 'L': #leaf
        turtle.showturtle()
        turtle.stamp()
        turtle.hideturtle()

l_system()

turtle.getscreen()._root.mainloop()  #prevents the screen from automatically closing after the turtle draws