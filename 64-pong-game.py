from turtle import Turtle,Screen
import random
from paddle64 import Paddle
from ball64 import Ball
import time
from scoreboard64 import Score


screen = Screen()
screen.setup(height =600, width = 800)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

paddle = Paddle((350,0))
tim =Paddle((-350,0))
ball = Ball() 
screen.listen()
score = Score()

screen.onkey(paddle.go_up,"Up")
screen.onkey(paddle.go_down,"Down")
screen.onkey(tim.go_up,"w")
screen.onkey(tim.go_down,"s")



end =True
while end: 
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.y_bounce()
    if ball.distance(paddle) <50 and   ball.xcor()>320 or ball.distance(tim)<50 and ball.xcor()<-320:
        ball.x_bounce()
    
    if ball.xcor() > 380 :
        ball.replace() 
        score.update() 
        
    if ball.xcor() < -380:
        ball.replace()
        score.update_2() 
              
        
screen.exitonclick()