import turtle
from math import cos, sin, radians
import random

# Global variable to keep track of the current level
current_level = 1
obstacles = []
drawing = True  # Flag to indicate whether drawing is in progress

# Function to move the turtle forward, but only if it stays within the maze boundaries and avoids obstacles
def move():
    global drawing  # Access the global drawing flag
    if drawing:
        return  # Do not move while drawing

    turtle.penup()
    new_x, new_y = calculate_new_position()
    crash = is_collision(new_x, new_y)
    
    if current_level == 1 and is_within_boundaries(new_x, new_y, margin=2):
        turtle.goto(new_x, new_y)
    elif current_level > 1 and is_within_boundaries(new_x, new_y, margin=2) and not crash:
        turtle.goto(new_x, new_y)
    elif crash:
        for obstacle in obstacles:
            obstacle_x, obstacle_y, obstacle_rad, obstacle_turtle = obstacle
            if obstacle_x - 20 <= new_x <= obstacle_x + 20 and obstacle_y - 20 <= new_y <= obstacle_y + 20:
                clear_obstacle(obstacle_turtle)
                draw_colored_circle(obstacle_x - obstacle_rad, obstacle_y + obstacle_rad, obstacle_rad)
        turtle.goto(new_x, new_y)
    turtle.update() 
# Function to calculate the new position after a move
def calculate_new_position():
    angle = turtle.heading()
    x, y = turtle.position()
    new_x = x + 30 * (cos(radians(angle)))
    new_y = y + 30 * (sin(radians(angle)))
    return new_x, new_y

# Function to clear the obstacle
def clear_obstacle(obstacle_turtle):
    obstacle_turtle.clear()

# Function to check if the new position is within the maze boundaries with a specified margin
def is_within_boundaries(x, y, margin=0):
    return -152 + margin <= x <= 152 - margin and -152 + margin <= y <= 152 - margin

# Function to check if the turtle collides with an obstacle
def is_collision(x, y):
    # Add your obstacle coordinates here
    for obstacle in obstacles:
        obstacle_x, obstacle_y, obstacle_rad, _ = obstacle
        if obstacle_x - 20 <= x <= obstacle_x + 20 and obstacle_y - 20 <= y <= obstacle_y + 20:
            return True  # Collision with obstacle
    return False

# Function to draw a colored circle
def draw_colored_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    random_color = (random.random(), random.random(), random.random())
    turtle.fillcolor(random_color)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

# Function to create random obstacles for levels greater than 1
def create_obstacles():
    global obstacles
    obstacles = []
    if current_level > 1:
        for _ in range(current_level + 1):
            obstacle_x = random.randint(-132, 132)  # At least 20 away from the border
            obstacle_y = random.randint(-132, 132)  # At least 20 away from the border
            obstacle_rad = random.randint(10, 20)  # Radius between 10 and 20
            # Ensure obstacles are at least 20 apart from each other
            while any(
                (
                    abs(obstacle_x - x) < 20 and abs(obstacle_y - y) < 20
                    for x, y, _, _ in obstacles
                )
            ) or not is_within_boundaries(obstacle_x, obstacle_y, margin=20):
                obstacle_x = random.randint(-132, 132)
                obstacle_y = random.randint(-132, 132)
            obstacle_turtle = turtle.Turtle()
            obstacles.append((obstacle_x, obstacle_y, obstacle_rad, obstacle_turtle))
            obstacle_turtle.speed(0)
            obstacle_turtle.hideturtle()
            obstacle_turtle.penup()
            obstacle_turtle.goto(obstacle_x, obstacle_y)
            draw_colored_circle(obstacle_x, obstacle_y, obstacle_rad)
    print(obstacles)

# Function to start drawing
def start_drawing():
    global drawing
    drawing = True

# Function to stop drawing
def stop_drawing():
    global drawing
    drawing = False

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

# Function to draw the maze and obstacles for level 1
def draw_maze_level1():
    start_drawing()
    turtle.clear()
    turtle.penup()
    turtle.goto(-152, 152)
    turtle.pendown()
    turtle.forward(304)
    turtle.right(90)
    turtle.forward(304)
    turtle.right(90)
    turtle.forward(304)
    turtle.right(90)
    turtle.forward(304)
    turtle.right(90)
    title = "Turtle Maze - Level " + str(current_level)
    # Display information and instructions
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.write(title, align="center", font=("Arial", 18, "normal"))

    turtle.penup()
    turtle.goto(0, 180)
    turtle.pendown()
    turtle.write("Navigate the turtle through the maze! Press the arrow keys to move. Press 'Q' to quit.",
                 align="center", font=("Arial", 12, "normal"))
    if current_level == 1:
        stop_drawing()
# Function to draw the maze and obstacles for level 2
def draw_maze_level2():
    turtle.clear()
    draw_maze_level1()  # Reuse the level 1 maze
    create_obstacles()  # Create random obstacles for level 2
    # Display level 2 information
    turtle.penup()
    turtle.goto(0, 160)
    turtle.pendown()
    turtle.write("Welcome to Level 2! New challenges await.", align="center", font=("Arial", 12, "normal"))
    stop_drawing()
# Set up the turtle screen
turtle.speed(2)

# Draw initial maze and information for the current level
draw_maze_level1()

# Set the starting position inside the maze
turtle.penup()
turtle.goto(-140, 140)  # Adjust the starting position
turtle.pendown()


# Keyboard bindings
if not drawing:
    print("not drawing")
    turtle.listen()
    turtle.onkey(turn_up, "Up")
    turtle.onkey(turn_down, "Down")
    turtle.onkey(turn_left, "Left")
    turtle.onkey(turn_right, "Right")
    turtle.onkey(turtle.bye, "Q")  # Press 'Q' to quit
turtle.onkey(start_drawing, "s")  # Press 's' to start drawing
turtle.onkey(stop_drawing, "x")   # Press 'x' to stop drawing

# Level switching function using keyboard events
def switch_levels():
    global current_level
    if current_level == 1:
        current_level = 2
        draw_maze_level2()
        turtle.penup()
        turtle.goto(-140, 140)  # Adjust the starting position
        turtle.pendown()
    else:
        current_level = 1
        draw_maze_level1()
        turtle.penup()
        turtle.goto(-140, 140)  # Adjust the starting position
        turtle.pendown()

# Bind the switch_levels function to the 'L' key
turtle.onkey(switch_levels, "L")
turtle.onkey(switch_levels, "l")

# Keep the window open
turtle.mainloop()
