from turtle import  Turtle
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_Score=0
        self.R_Score=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.L_Score, align="center", font=("Courier", 75, "normal"))
        self.goto(100, 200)
        self.write(self.R_Score, align="center", font=("Courier", 75, "normal"))
    def add_L_Score(self):
        self.L_Score+=1
        self.clear()
        self.update_scoreboard()
    def add_R_Score(self):
        self.R_Score+=1
        self.clear()
        self.update_scoreboard()



