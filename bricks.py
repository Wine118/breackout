from turtle import Turtle
import random

COLOR_LIST = [
    'red','green','purple'
]

weights = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
]

class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('square')

        # Random width between 20 to 50 units
        random_width = random.uniform(3,5)  # Random stretch_len between 1 and 2.5
        self.shapesize(stretch_wid=1.5, stretch_len=random_width)

        self.color(random.choice(COLOR_LIST))
        self.goto(x=x_cor, y=y_cor)

        

        # Calculate the brick's actual width in turtle units
        self.brick_width = random_width * 20  # Each unit of stretch_len equals 20 units

        # Defining borders of the brick
        self.left_wall = self.xcor() - (self.brick_width / 2)
        self.right_wall = self.xcor() + (self.brick_width / 2)
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15

        self.quantity = random.choice(weights)


class Bricks:
    def __init__(self):
        self.y_start = 0 # Start from the bottom
        self.y_end = 250  # Fill bricks up to the top of the screen
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        x_start = -570
        while x_start < 700:
            brick = Brick(x_start, y_cor)
            self.bricks.append(brick)
            x_start += brick.brick_width + 10 # Add a small gap between bricks

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 35):
            self.create_lane(i)

