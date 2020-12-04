import turtle
import random
from time import sleep
turtle.setup(width=1.0, height=1.0)
turtle.speed(30)
turtle.hideturtle()


def introPage():
    turtle.hideturtle()
    turtle.bgcolor("black")
    turtle.color("White")
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write(
        "Midterm Project", font=("Arial", 24, "italic"), align="center")
    turtle.right(90)
    turtle.forward(100)
    turtle.write(
        "Capricorn Constellation",
        font=("Arial", 24, "italic"),
        align="center")
    turtle.forward(100)
    turtle.write("Sade Richards", font=("Arial", 24, "italic"), align="center")
    sleep(20)
    turtle.clearscreen()


def Capricorn():
    turtle.hideturtle()
    turtle.clearscreen()
    turtle.pu()
    turtle.setposition(0, 100)
    turtle.pd()
    turtle.bgcolor("black")
    turtle.bgpic("seagoat.gif")
    turtle.update()
    sleep(20)
    turtle.clearscreen()


myPen = turtle.Turtle()
"""
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#000088")
"""

def drawConstellation(constellation):
    #draw the first star
    myPen.penup()
    myPen.goto(constellation[0])
    myPen.begin_fill()
    myPen.circle(2)
    myPen.end_fill()
    myPen.pendown()
    #draw each line and star within the constellation
    for star in constellation:
        myPen.goto(star)
        myPen.begin_fill()
        myPen.circle(2)
        myPen.end_fill()
    #hide the turtle


star1x = 25
star1y = -86
star2x = 49
star2y = -68
star3x = 112
star3y = 73
star4x = 106
star4y = 92
star5x = 113
star5y = 93
star6x = 106
star6y = 92
star7x = 4
star7y = 63
star8x = -78
star8y = 78
star9x = -99
star9y = 89
star10x = -51
star10y = -50
star11x = 25
star11y = -86


def dots():
  turtle.bgcolor("navy")
  myPen.penup()
  myPen.color("white")
  myPen.goto(star1x, star1y)
  myPen.dot(10)
  myPen.pendown()
  myPen.goto(star2x, star2y)
  myPen.dot(10)
  myPen.goto(star3x, star3y)
  myPen.dot(10)   
  myPen.goto(star4x, star4y)
  myPen.dot(10)
  myPen.goto(star5x, star5y)
  myPen.dot(10)
  myPen.goto(star6x, star6y)
  myPen.dot(10)
  myPen.goto(star7x, star7y)
  myPen.dot(10)
  myPen.goto(star8x, star8y)
  myPen.dot(10)
  myPen.goto(star9x, star9y)
  myPen.dot(10)
  myPen.goto(star10x, star10y)
  myPen.dot(10)
  myPen.goto(star11x, star11y)
  myPen.dot(10)
  sleep(30)

def drawStar(starsize, starcolor):
  turtle.color(starcolor)
  turtle.pendown()
  turtle.begin_fill()
  for side in range(5):
 		turtle.left(144)
 		turtle.forward(starsize)
  turtle.end_fill()
  turtle.penup()

def last():
  turtle.clearscreen()
  turtle.bgcolor("black")
  turtle.penup()
  turtle.hideturtle()
  turtle.goto(star1x,star1y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star2x,star2y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star3x,star3y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star4x,star4y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star5x,star5y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star6x,star6y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star7x,star7y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star8x,star8y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star9x,star9y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star10x,star10y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.goto(star11x,star11y)
  drawStar(20,"white")
  turtle.pendown()
  turtle.penup()
  turtle.goto(-155,123)
  drawStar(20,"yellow")
  turtle.pendown()
  turtle.penup()

  for star in range(25):
        moveToRandomLocation()
        drawStar(random.randint(5, 25), "yellow")
def moveToRandomLocation():
    turtle.penup()
    turtle.setpos(random.randint(-400, 400), random.randint(-400, 400))
    



introPage()
Capricorn()
dots()
last()
moveToRandomLocation()
