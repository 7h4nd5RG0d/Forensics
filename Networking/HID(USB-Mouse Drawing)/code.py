import turtle

def read_data_from_txt(txt_file):
    data = []
    with open(txt_file, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            data.append({"x": x, "y": y})
    return data

def draw_from_data(data):
    s = turtle.getscreen()
    s.screensize(100000, 10000)

    t = turtle.Turtle()
    t.pensize(1)
    t.penup()
    t.speed(5)

    for e in data:
        x = t.xcor()
        y = t.ycor()
        lxacc = e["x"]
        lyacc = e["y"]
        
        # Flip the x-coordinate to prevent mirroring
        lyacc = -lyacc
        
        t.setx(x + lxacc)
        t.sety(y + lyacc)

        # Assuming no button data from txt file, always pen down
        t.pendown()

def pause_drawing():
    global paused
    paused = not paused

def clear_drawing():
    turtle.clear()

# Read the data from the text file
txt_file = 'a.txt'
data = read_data_from_txt(txt_file)

# Draw using the extracted data
draw_from_data(data)

# Function to handle the 'p' key press event
def handle_pause():
    pause_drawing()

# Function to handle the 'r' key press event
def handle_resume():
    pause_drawing()

# Function to handle the 'c' key press event
def handle_clear():
    clear_drawing()

# Set up the screen and listen for key presses
screen = turtle.Screen()
screen.listen()

# Bind the handle_pause function to the 'p' key press event
screen.onkey(handle_pause, 'p')

# Bind the handle_resume function to the 'r' key press event
screen.onkey(handle_resume, 'r')

# Bind the handle_clear function to the 'c' key press event
screen.onkey(handle_clear, 'c')

# Main event loop
turtle.mainloop()
