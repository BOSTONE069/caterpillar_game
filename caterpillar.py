import turtle as t
import random as rd
import time as ti

t.bgcolor('yellow') #this is for defining the background color

caterpillar = t.Turtle() # this is for defining the turtle element
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()



leaf = t.Turtle() #This is for defining the leaf element
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14)) #This is about defining the coordinates of the leaf shape
t.register_shape('leaf', leaf_shape) # this is for regitering the defined shape
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()


game_started = False
text_turtle = t.Turtle()# this is for defining the text element in the project
text_turtle.write('Press SPACE to start', align='center', font=('Arial',18,'bold')) #this is about defining the elements of the text in the program
text_turtle.hideturtle()


score_turtle = t.Turtle() #this is for defining the score element in the project
score_turtle.hideturtle()
score_turtle.speed(0)


def outside_window(): # this is defined function for the area of the caterpillar to move within
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x,y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside

def place_leaf(): #This function for determining the postion of the leaf
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over(): #This function is supposed to show game over
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !', align='center', font=('Arial',30,'normal'))

def display_score(current_score): #This function shows the score in the game
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial',40,'bold'))


def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True: #This is the logic of the game on what happens to the caterpillar
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up(): # This defines the moves of the caterpillar
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down(): # This defines the moves of the caterpillar
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left(): # This defines the moves of the caterpillar
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)


def move_right():  # This defines the moves of the caterpillar
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
