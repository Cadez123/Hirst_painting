#import colorgram

# colors = colorgram.extract('image.jpeg', 88)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
import  random

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]

# setup turtle
turtle.colormode(255)
timmy = Turtle()
timmy.shape('turtle')
timmy.pensize(1)

# get to the bottom left corner
timmy.speed(0)
timmy.penup()
timmy.right(90)
timmy.forward(380)
timmy.right(90)
timmy.forward(460)
timmy.right(180)

# start drawing instantly
timmy.speed(0)
timmy.pendown()

# Draw a line of 10 dots
def complete_a_row():
    for x in range(10):
        color = random.choice(color_list)
        timmy.dot(20,color)
        timmy.penup()
        timmy.forward(70)
        timmy.pendown()

# Draw a row of lines and go to beginning of next line 10 times
for x in range(10):
    complete_a_row()
    timmy.penup()
    timmy.left(90)
    timmy.forward(70)
    timmy.left(90)
    timmy.forward(700)
    timmy.right(180)

screen = Screen()
screen.exitonclick()