

#Reddit [08/08/13] Challenge #131 [Intermediate] Simple Ray-Casting
#http://www.reddit.com/r/dailyprogrammer/comments/1jz2os/080813_challenge_131_intermediate_simple/
"""
 (Intermediate): Simple Ray-Casting
Ray Casting is a method of rendering 3D computer graphics, popular in the early/mid 90's. Famous games like \
Wolfenstein and Doom are great examples of ray-casting based graphics. Real-time computer graphics today are\
based on hardware-accelerated polygon rasterization, while film-quality computer graphics are based on \
ray-tracing (a more advanced and finer-detailed ray-casting derivative).
Your goal is to implement a single ray-cast query within a 2D world: you will be given the ray's origin and \
direction, as well as a top-down view of a tile-based world, and must return the position of the first wall\
you hit. The world will be made of a grid of tiles that are either occupied (as defined by the 'X' character),\  or empty (as defined by the space ' ' character). Check out these graphics as a visualization of example 1; it \
should help clarify the input data. Real ray-casting applications do many of these wall-collision hits,\
generally one per column of pixels you want to render, but today you only have to solve for a single ray!
Original author: /u/nint22
Formal Inputs & Outputs
Input Description
On standard console input you will be given two integers, N and M. N is the number of columns, while M is the number of rows. This will be followed by N rows of either M-characters 'x' or ' ' (space), where 'x' is a wall that you can collide with or ' ' which is empty space. After this world-definition data, you will be given three space-delimited floating-point values: X, Y, and R. X and Y are world positions, following this coordinate system description, with R being a radian-value degree representing your ray direction (using the unit-circle definition where if R is zero, it points to the right, with positive R growth rotation counter-clockwise). R is essentially how much you rotate the ray from the default position of X+ in a counter-clockwise manner.
Output Description
Simply print the collision coordinate with three-digit precision.
Sample Inputs & Outputs
Sample Input
Note that this input is rendered and explained in more detail here.
10 10
xxxxxxxxxx
x  x x   x
x  x x   x
x    x xxx
xxxx     x
x  x     x
x        x
x  x     x
x  x    xx
xxxxxxxxxx
6.5 6.5 1.571
Sample Output
6.500 1.000"
"""
#My Solution-----------------------------------------------------------------------
import math
f = open("challenge131.txt")
lines = [x.strip() for x in (f).readlines()]

size = (int(lines[0].split()[0]),int(lines[0].split()[1]))
board = [line for line in lines if line[0] == "x"]
start_position = (float(lines[size[1]+1].split()[0]),float(lines[size[1]+1].split()[1]))
vector = float(lines[size[1]+1].split()[2])

def move_amounts(vector):
    return math.cos(vector),math.sin(vector)

def move(position, vector, accuracy):
    return(position[0]+(move_amounts(vector)[0]/accuracy),position[1]-(move_amounts(vector)[1]/accuracy))

def find_collision(board,start_position,vector):
    current_position = start_position
    while True:
        current_position = move(current_position,vector,1000)
        if board[int(current_position[1])][int(current_position[0])] == "x":
            return current_position

print (find_collision(board,start_position,vector))


