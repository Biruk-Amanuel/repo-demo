import turtle

def draw_square(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
#can you define another function so that it can draw multiple squares in 360 degrees around a circle
def draw_multiple_squares(num_squares, length):
    angle = 360 / num_squares
    for _ in range(num_squares):
        draw_square(length)
        turtle.right(angle)

def draw_multiple_squares_with_params(num_squares, length, angle):
    for _ in range(num_squares):
        draw_square(length)
        turtle.right(angle)

# Get user input for angle and length
num_squares = int(input("Enter number of squares: "))
length = int(input("Enter length of each square: "))
angle = float(input("Enter angle between squares: "))

draw_multiple_squares_with_params(num_squares, length, angle)
# Example usage:
draw_square(100)
turtle.done()
