
import turtle
turtle.colormode(255)
import random

tim=turtle.Turtle()
colors_list=[(198, 166, 109), (141, 77, 54), (73, 98, 123), (158, 148, 54), (213, 203, 144), (120, 39, 29), (137, 160, 179), (70, 108, 74), (144, 176, 139), (195, 91, 70), (69, 52, 46), (96, 81, 89), (60, 52, 56), (224, 177, 163), (102, 141, 131), (97, 130, 164), (156, 141, 159), (49, 60, 83), (73, 67, 50), (111, 38, 42), (47, 56, 72), (108, 136, 140), (182, 199, 183), (182, 190, 205), (168, 101, 106), (51, 76, 61)]
tim.speed("fastest")
tim.setheading(45+180)
tim.penup()
tim.forward(250)
tim.pendown()
tim.setheading(0)

for i in range(10):
 for j in range(10):
     tim.dot(20, random.choice(colors_list))
     tim.penup()
     tim.forward(50)
     tim.pendown()
 tim.penup()
 tim.forward(-500)
 tim.left(90)
 tim.forward(50)
 tim.right(90)
 tim.pendown()

screen=turtle.Screen()
screen.exitonclick()








screen = turtle_module.Screen()
screen.exitonclick()

