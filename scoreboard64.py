from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle_score = 0
        self.tim_score = 0
        self.board()
        
    def board(self):    
        self.clear()
        self.goto(-100,200)
        self.write(self.paddle_score, align = "center", font=("Courier", 80 , "normal"))
        self.goto(100,200)
        self.write(self.tim_score, align = "center", font=("Courier", 80 , "normal"))
        
    def update(self):
       self.paddle_score += 1
       self.board()
    
    def update_2(self):
        self.tim_score += 1
        self.board()   
   