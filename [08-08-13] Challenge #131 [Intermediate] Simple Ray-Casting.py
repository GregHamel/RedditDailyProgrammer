

#[08-08-13] Challenge #131 [Intermediate] Simple Ray-Casting
#http://www.reddit.com/r/dailyprogrammer/comments/1jz2os/080813_challenge_131_intermediate_simple/

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


