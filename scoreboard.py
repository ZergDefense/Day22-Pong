from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, players, colors):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.players = players
        self.colors = colors
        self.show_players()
        self.update_board()

    def show_players(self):
        self.goto(-150, -280)
        self.color(self.colors[0])
        self.write(self.players[0], align="center", font=("Courier", 30, "normal"))
        self.color("white")
        self.goto(150, -280)
        self.color(self.colors[1])
        self.write(self.players[1], align="center", font=("Courier", 30, "normal"))
        self.color("white")

    def update_board(self):
        self.clear()
        self.show_players()
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.update_board()
