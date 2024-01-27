from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        # self.boundry()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", move = False,align = "center", font=('Arial', 15, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.high_score}", move = False,align = "center",
                   font=("Courier", 15, 'normal'))

    # def boundry(self):
    #     self.goto(0, 300)
    #     self.pendown()
    #     self.pensize(10)
    #     self.goto(297,300)
    #     for i in range(3):
    #         self.right(90)
    #         self.forward(600)
    #     self.right(90)
    #     self.goto(0,300)

    def update(self):
        self.score += 1
        self.update_score()
        # self.boundry()
