import turtle
screen = turtle.Screen() #object of the screen
t = turtle.Turtle() #object
t.shape("turtle")
t.pensize(8) #The size of the pen in pixs
t.pencolor("red") #colour
t.fillcolor("pink") #colour


t.begin_fill()
t.forward(180) #movement by pixels
t.left(90) #градус поворота а лево
t.forward(100) #movement by pixels
t.left(90) #градус поворота а лево
t.forward(180) #movement by pixels
t.left(90) #градус поворота а лево
t.forward(100) #movement by pixels
t.left(90) #градус поворота а лево
t.end_fill()

screen.exitonclick() # exit on click


