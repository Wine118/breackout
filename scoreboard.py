from turtle import Turtle

score = 0
FONT = ('arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        
        self.goto(x=-100, y=260)
        self.lives = lives
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} \
        | Lives: {self.lives}", align='left', font=FONT)

    def win(self):
        self.clear()
        self.write("You Win", align='left', font=FONT)

    def lose(self):
        self.clear()
        self.write("Game Over", align='left', font=FONT)    

    def increase_score(self):
        self.score += 1        
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    


# Example usage:
  # Set initial lives

