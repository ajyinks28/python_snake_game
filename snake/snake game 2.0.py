import turtle
import random
import time

# variables
delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.title("snake game")
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.tracer(0)

# screen border 
border_pen = turtle.Turtle()
border_pen.color("white")
border_pen.pensize(3)
border_pen.speed(0)
border_pen.penup()
border_pen.goto(-310, -310)
border_pen.pendown()
for i in range(4):
    border_pen.fd(620)
    border_pen.lt(90)
    border_pen.hideturtle()

# score borer pen
score_border = turtle.Turtle()
score_border.color("white")
score_border.pensize(3)
score_border.penup()
score_border.speed(0)
score_border.goto(-310, 260)
score_border.pendown()
score_border.fd(620)
score_border.hideturtle()

head = turtle.Turtle()
head.color("red")
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction ="stop"

segments = []

# pen for writing on screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score: 0  high score: 0", align = "center", font =("courier", 24, "normal"))


# food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

# defining game functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# key bindings
screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_right,"d")
screen.onkeypress(go_left,"a")



while True:
    screen.update()

# check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()> 240 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

# hide segments
        for segment in segments:
            segment.goto(1000, 1000)
# clear the segments
        segments.clear()

        # reset score
        score = 0
        # update scores

        pen.clear()
        pen.write("score: {}  high score: {}".format(score, high_score), align = "center", font =("courier", 24, "normal"))


# colloision with food
    if head.distance(food)< 20:
#moving the food to a random spot 
        x = random.randint(-290, 290)
        y=random.randint(-290, 260)
        food.goto(x, y)
# add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score: {}  high score: {}".format(score, high_score), align = "center", font =("courier", 24, "normal"))

#move the end segments first in revers order  
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
# move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)        

    move()    
# check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
# hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
# clear the segment list
            segments.clear()
            # reseting the scores
            score = 0

            pen.clear()
            pen.write("score: {}  high score: {}".format(score, high_score), align = "center", font =("courier", 24, "normal"))



    time.sleep(delay)



screen.mainloop()