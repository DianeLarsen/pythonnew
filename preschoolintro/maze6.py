import turtle
from math import cos, sin, radians

turtle.showturtle()
turtle.shape("turtle")

# Define the levels and current level
levels = [{'maze': 'maze4.png', 'start': (-175, 225)},
          {'maze': 'maze5.png', 'start': (-175, 225)},
          {'maze': 'maze6.png', 'start': (-175, 225)},
          {'maze': 'maze7.png', 'start': (-175, 225)},
          {'maze': 'maze8.png', 'start': (-175, 225)},
          {'maze': 'maze9.png', 'start': (-175, 225)},]
current_level = 0

# Function to load the maze for the current level
def load_maze():
    level_info = levels[current_level]
    turtle.bgpic(level_info['maze'])
    turtle.penup()
    turtle.goto(level_info['start'])
    turtle.pendown()
    turtle.pencolor("red")

# Function to display a congrats message and move to the next level
def congrats():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("blue")
    turtle.write("Congratulations! Level {} complete.".format(current_level + 1), align="center", font=("Arial", 16, "normal"))
    turtle.color("black")
    turtle.penup()
    turtle.goto(0, -20)
    turtle.write("Click to move to the next level.", align="center", font=("Arial", 12, "normal"))

# Function to move to the next level
def next_level(x, y):
    global current_level
    current_level += 1
    
    if current_level < len(levels):
        load_maze()
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.color("black")
        turtle.write("Level {} started.".format(current_level + 1), align="center", font=("Arial", 14, "normal"))
        turtle.ontimer(turtle.clear, 2000)  # Clear the message after 2 seconds
    else:
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.color("green")
        turtle.write("All levels complete! Click to start again.", align="center", font=("Arial", 16, "normal"))
        turtle.onscreenclick(restart_game)

# Function to restart the game
def restart_game(x, y):
    global current_level
    current_level = 0
    load_maze()
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("black")
    turtle.write("Game restarted. Level 1 started.", align="center", font=("Arial", 14, "normal"))
    turtle.ontimer(turtle.clear, 2000)  # Clear the message after 2 seconds
    
turtle.pendown()




def move():
    new_x, new_y = calculate_new_position()
    turtle.goto(new_x, new_y)

def calculate_new_position():
    angle = turtle.heading()
    x, y = turtle.position()
    new_x = x + 15 * (cos(radians(angle)))
    new_y = y + 15 * (sin(radians(angle)))
    return new_x, new_y
# Function to turn the turtle up
def turn_up():
    turtle.setheading(90)
    move()

# Function to turn the turtle down
def turn_down():
    turtle.setheading(270)
    move()

# Function to turn the turtle left
def turn_left():
    turtle.setheading(180)
    move()

# Function to turn the turtle right
def turn_right():
    turtle.setheading(0)
    move()

# Initialize the maze and listen for key events
load_maze()
turtle.listen()
turtle.onkey(turn_up, "Up")
turtle.onkey(turn_down, "Down")
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onscreenclick(next_level)

# press enter in the Terminal to exit the program
input()

