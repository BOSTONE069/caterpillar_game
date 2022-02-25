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


text_turtle = False # this is for defining the text element in the project
text_turtle = t.Turtle()
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
    lead.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over(): #This function is supposed to show game over
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !', align='center', font=('Arial',30,'normal'))

def display_score(): #This function shows the score in the game
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    score_turtle.write(str(current_score), align='right', font=('Arial',40,'bold'))



ti.sleep(10)
