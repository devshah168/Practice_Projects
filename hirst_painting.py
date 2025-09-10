from turtle import Turtle,Screen
import random
import turtle
# import colorgram
tim=Turtle()
tim.shape('arrow')
tim.color('blue')
turtle.colormode(255)
# rgb_colors=[]
# colors=colorgram.extract('image.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g= color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list=[
    (215, 166, 17),
    (205, 153, 99),
    (225, 205, 103),
    (161, 55, 101),
    (113, 187, 213),
    (154, 31, 58),
    (8, 109, 166),
    (42, 13, 24),
    (160, 29, 25),
    (12, 23, 52),
    (34, 122, 62),
    (59, 23, 18),
    (9, 32, 26),
    (186, 156, 173),
    (63, 166, 88),
    (171, 57, 42),
    (156, 208, 215),
    (94, 183, 167),
    (205, 99, 95),
    (240, 200, 3),
    (213, 174, 198),
    (28, 37, 105),
    (187, 99, 110),
    (163, 209, 197),
    (220, 177, 173),
    (14, 105, 56),
]
# def random_color():
#     r=random.randint(0,255)
#     g= random.randint(0, 255)
#     b= random.randint(0, 255)
#     random_color=(r,g,b)
#     return random_color
# colors=["black","red","yellow","blue","green","purple","brown","black"]
# i=0
# directions=[0,90,180,270]
# tim.pensize(15)
tim.speed("fastest")
# For drawing a square
# while i<4:
#     tim.forward(100)
#     tim.right(90)
#     i+=1

# For drawing a dashed line
# while i<20:
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     i+=1

# For drawing shapes from triangle to decagon
# for i in range (0,8):
#     tim.color(colors[i])
#     for _ in range (i+3):
#         tim.forward(100)
#         tim.right(360/(i+3))

# for drawing random diagram(Kind of like a snake)
# for _ in range(100):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# for drawing a spirograph
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading()+size_of_gap)
# draw_spirograph(5)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots=100
for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=Screen()
screen.exitonclick()
