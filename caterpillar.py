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
text_turtle.write('Press space to start', align='center', font=('Arial',18,'bold')) #this is about defining the elements of the text in the program
text_turtle.hideturtle()


score_turtle = t.Turtle() #this is for defining the score element in the project
score_turtle.hideturtle()
score_turtle.speed(0)






ti.sleep(10)
